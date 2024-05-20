from django.shortcuts import render, get_object_or_404
from blog.models import Post


# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    # <<----->> 13 and 14 lines are used as similar as line 16 <<----->>
    # post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)


def test(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/test.html', context)
