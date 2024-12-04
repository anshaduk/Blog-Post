from django.shortcuts import render
from .models import BlogPost
from .utils import get_user_country


def blog_post(request):
    client_country = get_user_country(request)
    posts = BlogPost.objects.all()
    filtered_posts = posts.filter(country=client_country) 

    context = {
        'posts': posts,
        'filtered_posts': filtered_posts,
        'country': client_country,
    }
    return render(request, 'blog/blog_post.html', context)

