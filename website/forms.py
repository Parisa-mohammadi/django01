from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=250)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

