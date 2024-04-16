import requests
from django.shortcuts import render


# Create your views here.

def resources(request):
    return render(request, "resource_page.html")


def dictionary(request):
    meanings = []

    if request.method == "POST":
        word = request.POST.get('word', '')
        word = word.capitalize()
        print(word)

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

    return render(request, 'dictionary.html', {'meanings': meanings, 'word': word})
