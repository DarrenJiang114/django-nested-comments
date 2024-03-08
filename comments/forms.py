from django import forms
from django.conf import settings

from .models import CommentVersion

import bleach

class CommentVersionForm(forms.ModelForm):
    class Meta:
        model = CommentVersion
        fields = ['message']
        
    def clean_message(self):
        message = self.cleaned_data['message']
        allowed_tags = settings.ALLOWED_TAGS if hasattr(settings, 'ALLOWED_TAGS') else settings.BLEACH_ALLOWED_TAGS if hasattr(settings, 'BLEACH_ALLOWED_TAGS ') else bleach.ALLOWED_TAGS
        allowed_attributes = settings.ALLOWED_ATTRIBUTES if hasattr(settings, 'ALLOWED_ATTRIBUTES') else settings.BLEACH_ALLOWED_ATTRIBUTES if hasattr(settings, 'BLEACH_ALLOWED_ATTRIBUTES ') else bleach.ALLOWED_ATTRIBUTES
        return bleach.clean(message, tags=allowed_tags, attributes=allowed_attributes, strip=True)