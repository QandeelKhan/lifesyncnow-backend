from django.contrib import admin
from .models import Category, BlogPost, Comment, Reply, Topic, TopicFeaturedPost
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
import admin_thumbnails


class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        model = BlogPost
        fields = '__all__'


@admin_thumbnails.thumbnail('cover_image')
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('title', 'slug', 'cover_image',)
    exclude = ('paragraphs', 'step_by_step_guides')


class CommentAdminForm(forms.ModelForm):
    comment_text = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        model = Comment
        fields = '__all__'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm


admin.site.register(Reply)
admin.site.register(TopicFeaturedPost)
admin.site.register(Topic)
admin.site.register(Category)
