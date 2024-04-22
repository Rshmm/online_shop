from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator


def post_list(request):
    post_list = Post.published.all()
    p = Paginator(post_list,4)
    page = request.GET.get('page')
    posts = p.get_page(page)

        
    return render(request, 'blog.html', {'post_list': post_list,
                                         'posts': posts})


def post_detail(request, year, month, day, post):
        post = get_object_or_404(Post,
                                status=Post.Status.PUBLISHED,
                                slug=post,
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
        return render(request, 'post_detail.html', {'post': post})
    