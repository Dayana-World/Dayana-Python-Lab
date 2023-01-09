from django import forms
from django.core.validators import ValidationError

from blog_post.models import Massage

# Create your forms
class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=50, label='Your name')
    text = forms.CharField(max_length=500, label='Your Massage')

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('same', code='same')


class MassageForm(forms.ModelForm):
    class Meta:
        model = Massage
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your title',
                'style': 'max-width: 300px;',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
            })
        }

    # or

    # title = forms.CharField(max_length=100)
    # text = forms.CharField(widget=forms.Textarea())
    # email = forms.EmailField()


