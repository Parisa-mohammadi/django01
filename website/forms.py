from django import forms
from website.models import Contact, Newsletter


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=250)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    # last_name = forms.CharField(max_length=255)
    # subject = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        # self.fields['subject'].required = False


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
