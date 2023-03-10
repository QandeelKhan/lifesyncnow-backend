from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView, CommentCreateView, ReplyCreateView

urlpatterns = [
    path('blog/posts-list', BlogPostListView.as_view(), name='blog-list'),
    path('<pk>/', BlogPostDetailView.as_view(), name='blog-detail'),
    path('create/', BlogPostCreateView.as_view(), name='blog-create'),
    path('<pk>/update/', BlogPostUpdateView.as_view(), name='blog-update'),
    path('<pk>/delete/', BlogPostDeleteView.as_view(), name='blog-delete'),
    path('<pk>/comments/', CommentCreateView.as_view(), name='post-comments'),
    path('<pk>/comments/<comment_id>/reply/',
         ReplyCreateView.as_view(), name='comment-reply'),
]
