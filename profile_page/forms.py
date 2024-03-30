from django import forms
from storages.backends.azure_storage import AzureStorage

from ALPP import settings
from .models import Profile, LearnerType


class LearnerTypeSettings(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['learner_type']

    learner_type = forms.ModelChoiceField(queryset=LearnerType.objects.all())


class ProfilePictureSettings(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic_url']

    def save(self, commit=True):
        instance = super().save(commit=False)
        profile_pic_url = self.cleaned_data.get('profile_pic_url')

        azure_storage = AzureStorage(
            account_name=settings.AZURE_ACCOUNT_NAME,
            account_key=settings.AZURE_ACCOUNT_KEY,
        )

        instance.profile_pic_url = azure_storage.save(profile_pic_url.name, profile_pic_url)

        if commit:
            instance.save()
        return instance
