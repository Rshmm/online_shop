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
    return render(request, 'post_detail.html', {'post': post})
    

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(post,id=post_id,status=Post.Status.PUBLISHED)
    comment = None
    # a comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # create a comment object without saving it to the database
        comment = form.save(commit=False)
        #assign the post to the comment
        comment.post = post
        # save the comment to the database
        comment.save()
    return render(request, 'comment.html',
                  {
                      'post' : post,
                      'form' : form,
                      'comment' : comment
                  })
    
