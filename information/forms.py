from django import forms
from .models import FeatureConfig, DevIteraction, DevelopmentList, Features, FeatureList

class FeatureConfigForm(forms.ModelForm):
    class Meta:
        model = FeatureConfig
        fields = [
            'key',
            'value'
        ]

class DevIteractionForm(forms.ModelForm):
    class Meta:
        model = DevIteraction
        fields = [
            'name',
            'main'
        ]

class DevelopmentListForm(forms.ModelForm):
    class Meta:
        model = DevIteraction
        fields = [
            'name'
        ]

class FeaturesForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = [
            'name'
        ]


class FeatureListForm(forms.ModelForm):
    class Meta:
        model = FeatureList
        fields = [
            'name'
        ]

