from django.urls import path
from blogging.views import BlogDetailView, BlogListView, stub_view


urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path(
        "posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"
    ),  # capture one or more digits as post_id
]
