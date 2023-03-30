from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView, CommentCreateView, ReplyCreateView, BlogPostByCategoryView, TopicListView, BlogPostListByCategoryAndTopicAPIView

urlpatterns = [
    path('blog/posts-list', BlogPostListView.as_view(), name='blog-list'),
    # path('blog/post/<pk>/', BlogPostDetailView.as_view(), name='blog-detail'),
    path('blog/category/<str:category_slug>/',
         BlogPostByCategoryView.as_view(), name='blog_post_by_category'),
    # path('blog/category/<str:category_slug>/<str:topic_slug>/',
    #      TopicListView.as_view(), name='blog_post_by_category'),
    path('blog/category/<str:category_slug>/<str:topic_slug>/',
         BlogPostListByCategoryAndTopicAPIView.as_view(), name='blog_post_by_category'),
    path('blog/post/<slug:slug>/', BlogPostDetailView.as_view(), name='blog-detail'),
    path('blog/post/create/', BlogPostCreateView.as_view(), name='blog-create'),
    path('blog/post/<pk>/update/', BlogPostUpdateView.as_view(), name='blog-update'),
    path('<pk>/delete/', BlogPostDeleteView.as_view(), name='blog-delete'),
    path('<pk>/comments/', CommentCreateView.as_view(), name='post-comments'),
    path('<pk>/comments/<comment_id>/reply/',
         ReplyCreateView.as_view(), name='comment-reply'),
]
