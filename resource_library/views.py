import requests
from django.contrib.auth.decorators import login_required
from django.contrib.humanize.templatetags import humanize
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from opentelemetry import trace
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes

from discussion_forums.utils import load_profanity_words, contains_profanity
from resource_library.models import Resource

PROFANE_WORDS = load_profanity_words('profanity.txt')

tracer = trace.get_tracer(__name__)


@login_required
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def resources(request):
    with tracer.start_as_current_span("resources", attributes={
        "http.method": request.method,
        "http.url": request.get_full_path(),
    }) as span:
        all_resources = Resource.objects.all().order_by('-added_at')
        for resource in all_resources:
            resource.humanized_added_at = humanize.naturaltime(resource.added_at)
            print(resource.humanized_added_at)

        if is_json_request(request):
            return json_response(all_resources)

        return render(request, "resources/resource_page.html", {'resources': all_resources})

def is_json_request(request):
    return 'application/json' in request.META.get('HTTP_ACCEPT', '') or request.content_type == 'application/json'

def json_response(resources):
    resources_data = [
        {
            'id': resource.id,
            'name': resource.name,
            'description': resource.description,
            'source': resource.source,
            'added_at': resource.added_at,
            'humanized_added_at': resource.humanized_added_at,
        }
        for resource in resources
    ]
    return JsonResponse({'resources': resources_data}, status=status.HTTP_200_OK, safe=False)


@login_required
def dictionary(request):
    with tracer.start_as_current_span("dictionary", attributes={
        "http.method": request.method,
        "http.url": request.get_full_path(),
    }) as span:
        meanings = []
        word = ""

        if request.method == "POST":
            word = request.POST.get('word', '')
            word = word.capitalize()
            print(word)

            if word == "Web" or word == ".net":
                meanings.append("Can I get a hundred from this subject, please? :3")
            if contains_profanity(word, PROFANE_WORDS):
                word = "..."
                meanings.append("You can't use this here.")

            response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

            if response.status_code == 200:
                data = response.json()

                for entry in data:
                    word_data = entry.get('word', '')

                    if word_data:
                        for meaning in entry.get('meanings', []):
                            definitions = meaning.get('definitions', [])

                            for definition in definitions:
                                meanings.append(definition.get('definition', ''))

        return render(request, 'resources/dictionary.html', {'meanings': meanings, 'word': word})
