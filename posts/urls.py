from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.Post_List, name="list"),
    path('<slug:slug>', views.Post_Page, name="page")
]