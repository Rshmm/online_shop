from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from django.core.paginator import Paginator
from blog.froms import CommentForm
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.db.models import Count 


def post_list(request):
    post_list = Post.published.all()
    p = Paginator(post_list,8)
    page = request.GET.get('page')
    posts = p.get_page(page)    
    return render(request, 'blog.html', {      
                                        'posts': posts
                                          })


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                            status=Post.Status.PUBLISHED,
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day,)
    comments = post.comments.filter(active=True)
    form = CommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                 .order_by('-same_tags','-publish')[:4]
    return render(request, 'post_detail.html', {'post': post,
                                                'comments' : comments,
                                                'form' : form,
                                                'similar_posts' : similar_posts
                                                })
    

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post,id=post_id,status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'comment.html',
                  {
                      'post' : post,
                      'form' : form,
                      'comment' : comment,
                  })
    
