from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    # tag
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return "{}-{}".format(self.title, self.id)

    def snipped(self):
        return 'this is snipped'

    """
    
    you can do this function in sitemaps.py as get_absolute_url(). Just dont forget to import reverse
    
    """
    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.id})
        
