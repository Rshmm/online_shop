from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from django.core.paginator import Paginator
from blog.froms import CommentForm
from django.views.decorators.http import require_POST


def post_list(request):
    post_list = Post.published.all()
    p = Paginator(post_list,8)
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
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request, 'post_detail.html', {'post': post,
                                                'comments' : comments,
                                                'form' : form
                                                })
    

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(post,id=post_id,status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'comment.html',
                  {
                      'post' : post,
                      'form' : form,
                      'comment' : comment
                  })
    
