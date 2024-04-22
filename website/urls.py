from  django.urls import path
from website.views import home, contact_view, about_view

urlpatterns = [
    path('', home),
    path('contact', contact_view),
    path('about', about_view)
]