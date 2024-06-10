from django.http import HttpResponse
from django.shortcuts import render
from website.forms import NameForm


def index_view(request):
    return render(request, 'website/index.html')


def contact_view(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
    form = NameForm()
    return render(request, 'website/contact.html', {'form': form})


def about_view(request):
    return render(request, 'website/about.html')


def test(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
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
            return HttpResponse("DONE")
        else:
            HttpResponse('Not valid')
    else:
        form = NameForm()
    return render(request, 'test.html', {'form': form})
