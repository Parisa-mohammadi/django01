from django import template
from blog.models import Post
from blog.models import Category
from django.utils import timezone

register = template.Library()


@register.simple_tag()
def sayHello():
    return 'Hello'


@register.simple_tag()
def function(a):
    return a + 2


@register.simple_tag(name='plus_two')
def function(a=5):
    return a + 2


@register.simple_tag(name='plus_2')
def function(a):
    return a + 2


@register.simple_tag(name='total_post')
def function():
    post = Post.objects.filter(status=1).count()
    return post


@register.simple_tag(name='posts')
def function():
    post = Post.objects.filter(status=1).count()
    return post


@register.filter
def snippet(value, arg=20):
    return value[:arg] + "..."


@register.inclusion_tag('blog/popularposts.html')
def popularposts():
    posts = Post.objects.filter(status=1).order_by('published_date')
    return {'posts': posts}


@register.inclusion_tag('blog/blog-popular-post.html')
def latestpost(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}


@register.inclusion_tag('blog/blog-index-latestposts.html')
def index_latestposts(arg=6):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts': posts}
