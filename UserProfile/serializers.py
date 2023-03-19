from rest_framework import serializers
from .models import UserProfile
from blog.serializers import BlogPostSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    blog_posts = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_blog_posts(self, obj):
        blog_posts = obj.user.blog_posts.all()
        return BlogPostSerializer(blog_posts, many=True).data
