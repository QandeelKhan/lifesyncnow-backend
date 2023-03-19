
from rest_framework import serializers
from .models import BlogPost, BlogPostImage, Comment, Reply, BlogStepByStepGuide, SubFields, SBSGuideSubSection, BlogParagraph


class SubFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubFields
        fields = '__all__'


class SBSGuideSubSectionSerializer(serializers.ModelSerializer):
    sub_headings_and_contents = SubFieldsSerializer(many=True)

    class Meta:
        model = SBSGuideSubSection
        fields = '__all__'


class SBSGuideSerializer(serializers.ModelSerializer):
    sbs_guides_subsections = SBSGuideSubSectionSerializer(many=True)

    class Meta:
        model = BlogStepByStepGuide
        fields = '__all__'


class BlogPostImageSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = BlogPostImage
        fields = '__all__'

    def get_images(self, obj):
        if obj.images:
            return self.context['request'].build_absolute_uri(obj.images.url)
        return None


class ReplySerializer(serializers.ModelSerializer):
    author_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Reply
        # fields = '__all__'
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

# class BlogPostSerializer(serializers.ModelSerializer):
#     post_images = BlogPostImageSerializer(many=True)
#     comments = CommentSerializer(many=True, read_only=True)

#     class Meta:
#         model = BlogPost
#         fields = '__all__'


class BlogParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogParagraph
        fields = ('id', 'paragraph_title', 'paragraph_content')


class BlogPostSerializer(serializers.ModelSerializer):
    paragraphs = BlogParagraphSerializer(
        source='blog_paragraphs.all', many=True)
    post_images = BlogPostImageSerializer(many=True)
    step_by_step_guide = SBSGuideSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    category_name = serializers.ReadOnlyField(source='category.category_name')

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'post_images',
            'comments',
            'comment_count',
            'title',
            'content',
            'cover_image',
            # 'initial_paragraph',
            # 'paragraph_heading',
            # 'second_paragraph',
            'paragraphs',
            'quote',
            'quote_writer',
            # 'paragraph_after_image',
            'author',
            'author_first_name',
            'author_last_name',
            'created_at',
            'updated_at',
            'category',
            'category_name',
            'most_recent_posts',
            'older_posts',
            'featured_posts',
            'step_by_step_guide',
            # 'sps_guide',
            'full_name',

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
