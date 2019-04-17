from django import forms
from .models import Url, SubClass

class CreateFormUrl(forms.ModelForm):

    class Meta:
        model = Url
        fields = ('site', 'site_name', 'subclass')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class CreateFormSubclass(forms.ModelForm):

    class Meta:
        model = SubClass
        fields = ('subclass',)
