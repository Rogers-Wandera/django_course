from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def Post_List(request: HttpRequest):
    return render(request, "posts/post_list.html")