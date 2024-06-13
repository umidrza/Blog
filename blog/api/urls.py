from django.urls import path
from .views import *

app_name = 'blog-api'

urlpatterns = [
    path("", BlogListAPIView.as_view(), name="list"),
    path("create/", BlogCreateAPIView.as_view(), name="create"),
    path("<pk>/", BlogDetailAPIView.as_view(), name="detail"),
    path("<pk>/update/", BlogUpdateAPIView.as_view(), name="update"),
    path("<pk>/delete/", BlogDeleteAPIView.as_view(), name="delete"),
]