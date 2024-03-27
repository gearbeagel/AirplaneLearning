from django import forms
from .models import Profile


class LearningPathSelectForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['learner_type', 'chosen_language']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['learner_type']
