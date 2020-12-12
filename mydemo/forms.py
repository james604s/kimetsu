from django.forms import ModelForm
from mydemo.models import MaskData

class MaskModelForm(ModelForm):
    class Meta:
        model = MaskData
        fields = ['city']