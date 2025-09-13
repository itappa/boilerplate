from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("upload/", views.upload, name="upload"),
    path("", views.ItemListView.as_view(), name="index"),
]
