from django import forms

from .models import Category, Tag, ScreenshotGroup, Screenshot
from .widgets import MultipleFileField


class ScreenshotGroupForm(forms.ModelForm):
    class Meta:
        model = ScreenshotGroup
        fields = ("title", "category", "tags")


class ScreenshotForm(forms.ModelForm):
    class Meta:
        model = Screenshot
        fields = ("image", "category", "tags")


class MultipleImageForm(forms.Form):
    image = MultipleFileField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tags = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False)
