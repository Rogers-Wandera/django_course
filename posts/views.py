from django.shortcuts import render
from django.http import HttpRequest
from .models import Post


def Post_List(request: HttpRequest):
    posts = Post.objects.all().order_by("-date")
    return render(request, "posts/post_list.html", {"posts": posts})