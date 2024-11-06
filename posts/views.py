from django.shortcuts import render
from django.http import HttpRequest
from .models import Post


def Post_List(request: HttpRequest):
    posts = Post.objects.all().order_by("-date")
    return render(request, "posts/post_list.html", {"posts": posts})

def Post_Page(request: HttpRequest, slug: str):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post_page.html", {"post": post})