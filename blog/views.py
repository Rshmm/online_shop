from django.shortcuts import render
from blog.models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog.html', {'posts': posts})


def post_detail(request , id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        return render(request,'404.html')
    
    return render(request, 'post_detail.html', {'post': post})