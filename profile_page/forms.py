from django import forms
from .models import Profile


# class LearningPathSelectForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['learner_type', 'chosen_language']


class LearnerTypeSettings(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['learner_type']


class ProfilePictureSettings(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic_url']
