
from rest_framework import serializers
from .models import BlogPost, Comment, Reply, Topic, TopicFeaturedPost, Category
from django.conf import settings
import re


# class BlogPostImageSerializer(serializers.ModelSerializer):
#     images = serializers.SerializerMethodField()

#     class Meta:
#         model = BlogPostImage
#         fields = '__all__'

#     def get_images(self, obj):
#         if obj.images:
#             return self.context['request'].build_absolute_uri(obj.images.url)
#         return None


class ReplySerializer(serializers.ModelSerializer):
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Reply
        fields = ['id', 'created_at', 'updated_at', 'reply_text', 'comment_id',
                  'author', 'author_full_name']
        depth = 1

    def get_author_first_name(self, obj):
        return obj.author.first_name

    def get_author_last_name(self, obj):
        return obj.author.last_name

    def get_author_full_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"


class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'comment_count', 'replies', 'created_date',
                  'updated_at', 'comment_text', 'post', 'author', 'author_first_name', 'author_last_name', 'author_full_name']
        depth = 1

    def get_author_first_name(self, obj):
        return obj.author.first_name

    def get_author_last_name(self, obj):
        return obj.author.last_name

    def get_author_full_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

    def get_comment_count(self, obj):
        return obj.replies.count()


class TopicFeaturedPostSerializer(serializers.ModelSerializer):
    # post = serializers.SerializerMethodField()

    class Meta:
        model = TopicFeaturedPost
        fields = ['featured_topic_type']
        # fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    topics_name = serializers.SerializerMethodField()
    topic_slug = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['category_name', 'category_slug',
                  'topics_name', 'topic_slug']

    def get_topics_name(self, obj):
        topics = obj.topics.all()
        return [topic.topic_name for topic in topics]

    def get_topic_slug(self, obj):
        topics = obj.topics.all()
        return [topic.topic_slug for topic in topics]


class TopicSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Topic

        fields = ['topic_name', 'topic_slug', 'category']

    def get_topics_name(self, obj):
        categories = obj.category.all()
        return [category.category_name for category in categories]


class FixImageUrlSerializerField(serializers.CharField):
    def to_representation(self, value):
        if value:
            # Regular expression to match image URLs
            pattern = r'<img([^>]*)src=["\']([^"\']+)["\']([^>]*)>'

            # Find all image URLs in the content field
            matches = re.finditer(pattern, value)

            # Fix the image URLs by adding the server URL and new class
            for match in matches:
                attrs = match.group(1)
                url = match.group(2)
                end_attrs = match.group(3)

                # Check if 'class' attribute is present
                if 'class' not in attrs:
                    attrs += ' class="ck-blog-content-img"'

                fixed_url = f'{settings.SERVER_URL}{url}'
                fixed_tag = f'<img{attrs} src="{fixed_url}"{end_attrs}>'

                value = value.replace(match.group(0), fixed_tag)

        return value


class BlogPostSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    topics_name = serializers.SerializerMethodField()
    topic_slug = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()
    content = FixImageUrlSerializerField()
    full_name = serializers.SerializerMethodField()
    category_name = serializers.ReadOnlyField(source='category.category_name')

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'author',
            'author_first_name',
            'author_last_name',
            'author_earnings',
            'content',
            'comments',
            'cover_image',
            'comment_count',
            'created_at',
            'category',
            'category_name',
            'full_name',
            'featured_posts',
            'most_recent_posts',
            'older_posts',
            'post_images',
            'slug',
            'title',
            'topic',
            'topics_name',
            'topic_slug',
            'updated_at',
        ]
        depth = 1

    def get_author_first_name(self, obj):
        return obj.author.first_name

    def get_author_last_name(self, obj):
        return obj.author.last_name

    def get_comment_count(self, obj):
        return obj.comments.count()

    def get_full_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

    def get_topics_name(self, obj):
        topics = obj.topic.category.topics.all()
        return [topic.topic_name for topic in topics]

    def get_topic_slug(self, obj):
        topics = obj.topic.category.topics.all()
        return [topic.topic_slug for topic in topics]

    def create(self, validated_data):
        request = self.context.get('request')
        if request:
            validated_data['author'] = request.user
        return super().create(validated_data)
