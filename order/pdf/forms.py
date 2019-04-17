from django import forms
from .models import Pdf

class CreatePdfForm(forms.ModelForm):

    class Meta:
        model = Pdf
        fields = ('title', 'pdf', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
