from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from website.forms import NameForm, ContactForm, NewsletterForm
from website.models import Contact
from django.contrib import messages
from django.views.generic.edit import UpdateView



def index_view(request):
    return render(request, 'website/index.html')


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_name = form.save(commit=False)
            new_name.name = 'anonymous'
            new_name.save()
            form.save()
            # messages.add_message(request, messages.SUCCESS, 'Submited successfully')
            messages.success(request, 'Submited successfully')
        else:
            messages.error(request, 'Not Submited')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def Newsletter_view(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')


def about_view(request):
    return render(request, 'website/about.html')


def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # email = request.POST.get('email')
        # message = request.POST.get('message')
        # c = Contact()
        # c.name = name
        # c.email = email
        # c.message = message
        # c.save()
        # print(name, email, message)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name, email, subject, message)
            form.save()
            return HttpResponse("DONE")
        else:
            HttpResponse('Not valid')
    form = ContactForm()
    return render(request, 'test.html', {'form': form})


MESSAGE_TAGS = {
    messages.INFO: "",
    50: "critical",
}
