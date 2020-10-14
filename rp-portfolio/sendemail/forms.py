from django import forms
from .models import Contact
from django.template.defaultfilters import slugify
#...

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
'''
STATUS_CHOICES = (
    ('d', 'Deals'),
    ('j', 'Jobs'),
)
class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Your name',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_email = forms.EmailField(label='Your email',max_length=100,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea, required=True),
    status = forms.ChoiceField(choices = STATUS_CHOICES)
'''
#contact_name = forms.CharField(required=True, label="Name")
#contact_email = forms.EmailField(required=True, label="Email")
