from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import BlogPost, Comment, Reply
from .serializers import BlogPostSerializer, CommentSerializer, ReplySerializer


class BlogPostListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


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


# class CommentCreateView(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CommentSerializer

#     def perform_create(self, serializer):
#         blog_post_id = self.kwargs['blog_post_id']
#         blog_post = BlogPost.objects.get(id=blog_post_id)
#         serializer.save(author=self.request.user, post=blog_post)


# class ReplyCreateView(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = ReplySerializer

#     def perform_create(self, serializer):
#         comment_id = self.kwargs['comment_id']
#         comment = Comment.objects.get(id=comment_id)
#         serializer.save(author=self.request.user, comment_id=comment)

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
