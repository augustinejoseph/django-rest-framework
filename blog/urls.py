from django.urls import base, include, path
from .views import PostList, PostDetail, Category

urlpatterns = [
    path("post/", PostList.as_view(), name="listview"),
    path("category/", Category.as_view(), name="category"),
    path("post/<int:pk>/", PostDetail.as_view(), name="detailview"),
]
