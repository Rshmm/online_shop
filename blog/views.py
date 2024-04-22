from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(post_list, 8)
    page_number = request.GET.get('get', 1)
    posts = paginator.page(page_number)
    return render(request, 'blog.html', {'posts': posts})


def post_detail(request, year, month, day, post):
        post = get_object_or_404(Post,
                                status=Post.Status.PUBLISHED,
                                slug=post,
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
        return render(request, 'post_detail.html', {'post': post})
    