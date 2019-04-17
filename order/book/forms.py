from django import forms
from .models import BookInfo

class CreateImageForm(forms.ModelForm):

    class Meta:
        model = BookInfo
        fields = ('title', 'amazon_url', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
