from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def contact_view(request):
    return HttpResponse("<h1>Contact Us</h1>")

def about_view(request):
    return HttpResponse("<h1>About Us</h1>")