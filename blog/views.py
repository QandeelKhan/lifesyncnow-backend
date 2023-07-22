import json
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import BlogPost, Comment, Reply, Topic, Category
from .serializers import BlogPostSerializer, CommentSerializer, ReplySerializer, Topic, TopicSerializer
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .tasks import clear_blogpost_list_cache
import time
from django.http import JsonResponse
from django.http import HttpResponse
from .tasks import load_posts_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.views.decorators.http import require_GET


class BlogPostByCategoryView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):

        category_slug = self.kwargs.get('category_slug')
        return BlogPost.objects.filter(category__category_slug=category_slug)


# @cache_page(60 * 15)  # Cache the view for 15 minutes
class BlogPostListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query)
            )
        return queryset
    # introducing cache key "blogpost_list" for this view, and initializing caching in this view.
    # in func based views by default we use "def get" with @cache_page on top but it's a class based so it include that get func inside the list func to introduce cache

    def list(self, request, *args, **kwargs):
        cache_key = 'blogpost_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            # Measure response time for cached response
            start_time = time.time()
            response = Response(cached_data)
            end_time = time.time()
            response_time = end_time - start_time
            print(
                f"Already initialized Cached Response time: {response_time} seconds")
        else:
            start_time = time.time()
            response = super().list(request, *args, **kwargs)
            end_time = time.time()
            response_time = end_time - start_time
            print(
                f"initialization of caching Response time: {response_time} seconds")

            # Cache the response for future requests
            cache.set(cache_key, response.data)

        return response


@require_GET
def enqueue_load_posts(request):
    # Enqueue the task and retrieve the task ID
    task = load_posts_task.delay()

    # Store the task ID in the cache
    cache.set('load_posts_task_id', task.id)

    return JsonResponse({'task_id': task.id})
    # Return the task ID as a plain string response
    # return HttpResponse(task.id, "Task enqueued successfully")
    # return HttpResponse("Task enqueued successfully")


# class BlogPostListView(generics.ListAPIView):
#     permission_classes = [AllowAny]
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         search_query = self.request.query_params.get('search', None)
#         if search_query:
#             queryset = queryset.filter(
#                 Q(title__icontains=search_query) |
#                 Q(content__icontains=search_query)
#             )
#         return queryset

#     def list(self, request, *args, **kwargs):
#         cache_key = 'blogpost_list'
#         cached_data = cache.get(cache_key)
#         if cached_data:
#             # Measure response time for cached response
#             start_time = time.time()
#             response = Response(cached_data)
#             end_time = time.time()
#             response_time = end_time - start_time
#             print(
#                 f"Already initialized Cached Response time: {response_time} seconds")
#         else:
#             start_time = time.time()
#             queryset = self.get_queryset()

#             # Calculate the total number of posts
#             total_posts = queryset.count()
#             loaded_posts = 0

#             # Create a channel layer to communicate with WebSocket consumer
#             channel_layer = get_channel_layer()

#             # Retrieve the task ID from cache
#             task_id = cache.get('load_posts_task_id')

#             if task_id:
#                 # Iterate through each post and send progress updates
#                 for post in queryset:
#                     # Load the post
#                     # ...

#                     # Increment the loaded posts counter
#                     loaded_posts += 1

#                     # Calculate the progress percentage
#                     progress = int((loaded_posts / total_posts) * 100)

#                     # Send progress update to WebSocket consumer
#                     async_to_sync(channel_layer.group_send)(
#                         # f'progress_{task_id}',  # Group name based on task ID
#                         # Group name based on task ID
#                         f'progress_{self.request.id}',
#                         {
#                             'type': 'send_progress_update',
#                             'progress': progress,
#                         }
#                     )

#                 # Cache the response for future requests
#                 response = super().list(request, *args, **kwargs)
#                 cache.set(cache_key, response.data)

#                 end_time = time.time()
#                 response_time = end_time - start_time
#                 print(
#                     f"Initialization of caching Response time: {response_time} seconds")
#             else:
#                 # Return empty response if task ID is not available
#                 response = Response([])

#         return response


class BlogPostDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # lookup_fields = ['slug', 'pk']
    lookup_field = 'slug'

    # def get_absolute_url(self):
    #     """
    #     Returns the absolute URL of the blog post.
    #     """
    #     return reverse("blog:post_detail", kwargs={"slug_field": self.slug_field})
    def retrieve(self, request, *args, **kwargs):
        # Check if the response is already cached
        cache_key = f'blogpost_detail_{kwargs["slug"]}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        # If not cached, retrieve the response from the superclass (super().retrieve)
        else:
            response = super().retrieve(request, *args, **kwargs)

            # Cache the response for future requests
            cache.set(cache_key, response.data)

            return response


class TopicListView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'topic_slug'

    # @cache_page(60 * 60 * 24)  # Cache for 24 hours
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BlogPostListByCategoryAndTopicAPIView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        topic_slug = self.kwargs.get('topic_slug')
        category = get_object_or_404(Category, category_slug=category_slug)
        topic = get_object_or_404(
            Topic, topic_slug=topic_slug, category=category)
        queryset = BlogPost.objects.filter(topic=topic)
        return queryset

# BlogPostDetailView:


class BlogPostCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class CommentCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def post(self, request, post_id):
        comment_text = request.data.get('comment_text')
        if not comment_text:
            return Response({'comment_text': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            blog_post = BlogPost.objects.get(id=post_id)
        except BlogPost.DoesNotExist:
            return Response({'error': 'The blog post does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        comment = Comment.objects.create(
            post=blog_post,
            author=request.user,
            comment_text=comment_text
        )
        serializer = self.serializer_class(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReplyCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReplySerializer

    def post(self, request, comment_id):
        reply_text = request.data.get('reply_text')
        if not reply_text:
            return Response({'reply_text': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({'error': 'The comment does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        reply = Reply.objects.create(
            comment_id=comment,
            author=request.user,
            reply_text=reply_text
        )
        serializer = self.serializer_class(reply)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
