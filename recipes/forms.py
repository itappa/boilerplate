from django import forms

from .models import Category, Tag, RecipeGroup, RecipeImage
from .widgets import MultipleFileField


class RecipeGroupForm(forms.ModelForm):
    class Meta:
        model = RecipeGroup
        fields = ("title", "category", "tags")


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ("image", "category", "tags")


class MultipleImageForm(forms.Form):
    image = MultipleFileField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tags = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False)
