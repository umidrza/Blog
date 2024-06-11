from django.urls import path
from .views import *

app_name = 'blog-api'

urlpatterns = [
    path("", BlogListAPIView.as_view(), name="list"),
    path("create/", BlogCreateAPIView.as_view(), name="create"),
    path("detail/<pk>", BlogDetailAPIView.as_view(), name="detail"),
    path("update/<pk>", BlogUpdateAPIView.as_view(), name="update"),
    path("delete/<pk>", BlogDeleteAPIView.as_view(), name="delete"),
]