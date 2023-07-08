from rest_framework import serializers
from .models import UserProfile
from blog.serializers import BlogPostSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    # blog_posts = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    role_name = serializers.SerializerMethodField()
    related_posts = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['user', 'email', 'bio', 'user_slug', 'first_name', 'last_name', 'full_name', 'profile_image', 'role', 'role_name', 'country',
                  'city', 'twitter_acc', 'facebook_acc', 'instagram_acc', 'related_posts']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def get_role_name(self, obj):
        if obj.role:
            return obj.role.role_name
        # if role field have no value
        return None

    def get_related_posts(self, obj):
        posts = obj.user.blog_posts.all()
        # deriving the project base url to add it with images as by default it can show image urls like /media/cover_image etc without including the localhost:8000/media.... which is valid
        request = self.context.get('request')
        base_url = request.build_absolute_uri('/')[:-1] if request else ''
        return [
            {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'slug': post.slug,
                'created_at': post.created_at,
                'updated_at': post.updated_at,
                'category_name': post.category.category_name,
                'author_first_name': post.author.first_name,
                'author_last_name': post.author.last_name,
                'comment_count': post.comments.count(),
                'cover_image': f"{base_url}{post.cover_image.url}" if post.cover_image else None,
            }
            for post in posts
        ]

    # In this example, related_posts is defined as a serializers.SerializerMethodField() that uses a custom method get_related_posts to retrieve the related posts for the user, and return a list of dictionaries with the desired fields. Note that we need to include the id field in the dictionary to be able to retrieve individual blog posts later, if needed. Also, note that we are using the url attribute of the cover_image field to serialize the cover image, if it exists. If the cover_image field is None, we set it to None in the dictionary.
