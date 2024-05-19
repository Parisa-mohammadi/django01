from django.db import models


# Create your models here.
class Post(models.Model):
    # author
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=1000)
    # image
    # tag
    # category = models.CharField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return "{}-{}".format(self.title, self.id)
