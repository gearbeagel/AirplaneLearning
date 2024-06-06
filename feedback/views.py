import os

from azure.storage.blob import BlobServiceClient
from django.shortcuts import render
from opentelemetry import trace

from ALPP import settings
from .forms import FeedbackForm

tracer = trace.get_tracer(__name__)


def feedback(request):
    with tracer.start_as_current_span("feedback") as span:
        success_message = ''
        form = FeedbackForm()
        if request.method != 'POST':
            context = {
                'form': form,
                'success_message': success_message,
            }
            return render(request, 'misc/feedback.html', context)
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            success_message = "Form filled out successfully!"
            feedback_form = form.save(commit=False)
            feedback_form.profile = request.user.profile

            screenshot = request.FILES.get('screenshot')
            if screenshot:  # Check if screenshot is not None
                blob_service_client = BlobServiceClient.from_connection_string(os.getenv('connection_str'))
                container_client = blob_service_client.get_container_client(settings.AZURE_CONTAINER)

                blob_name = f"screenshot_{screenshot.name}"  # Use screenshot name

                blob_client = container_client.get_blob_client(blob_name)
                blob_client.upload_blob(screenshot)

                feedback_form.screenshot = blob_client.url  # Set screenshot URL in feedback_form

            feedback_form.save()

        context = {
            'form': form,
            'success_message': success_message,
        }
        return render(request, 'misc/feedback.html', context)
