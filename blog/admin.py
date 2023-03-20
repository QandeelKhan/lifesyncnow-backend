# from django.contrib import admin
# from .models import BlogPostImage, BlogPost, Category, Comment, Reply

# # Register your models here.

# from django import forms
# from django.forms import ClearableFileInput, MultiValueField, ImageField, MultiWidget


# class BlogPostImageForm(forms.ModelForm):
#     class Meta:
#         model = BlogPostImage
#         fields = ['images', 'image_links']


# class BlogPostImageWidget(ClearableFileInput, forms.TextInput):
#     pass


# class BlogPostAdminForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = '__all__'

#     post_images = MultiValueField(
#         widget=MultiWidget(
#             widgets=(
#                 BlogPostImageWidget(attrs={'multiple': True}),
#                 forms.TextInput()
#             )
#         ),
#         fields=(
#             ImageField(),
#             forms.CharField()
#         ),
#     )

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance.pk:
#             initial_images = BlogPostImage.objects.filter(
#                 blog_post=self.instance)
#             self.fields['post_images'].widget = MultiWidget(
#                 widgets=(
#                     BlogPostImageWidget(attrs={'multiple': True}),
#                     forms.TextInput()
#                 )
#             )
#             self.fields['post_images'].initial = [
#                 (image.image, image.image_link) for image in initial_images
#             ]

#     def save(self, commit=True):
#         blog_post = super().save(commit=False)
#         if commit:
#             blog_post.save()

#         if self.cleaned_data.get('post_images'):
#             images_and_links = self.cleaned_data['post_images']
#             for image, image_link in images_and_links:
#                 BlogPostImage.objects.create(
#                     blog_post=blog_post, image=image, image_link=image_link
#                 )


# class BlogPostAdmin(admin.ModelAdmin):
#     form = BlogPostAdminForm


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['category_name']
#     ordering = ['category_name']


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['post', 'author_name', 'created_date', 'updated_at']
#     search_fields = ['post', 'author_name']
#     list_filter = ['created_date', 'updated_at']
#     ordering = ['created_date']


# class ReplyAdmin(admin.ModelAdmin):
#     list_display = ['comment', 'author', 'created_at', 'updated_at']
#     search_fields = ['comment', 'author']
#     list_filter = ['created_at', 'updated_at']
#     ordering = ['created_at']


# admin.site.register(BlogPost, BlogPostAdminForm)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Comment, CommentAdmin)
# admin.site.register(Reply, ReplyAdmin)
from django.contrib import admin
from .models import Category, BlogPost, BlogPostImage, Comment, Reply, TopicType
from .paragraph_with_sbs import BlogStepByStepGuide, BlogParagraph

# Register your models here.
# admin.site.register(Category)
# # admin.site.register(BlogPost)


# # @admin.register(BlogStepByStepGuide)
# class SBSGuideSubSectionInline(admin.TabularInline):
#     model = SBSGuideSubSection
#     extra = 1


# @admin.register(SBSGuideSubSection)
# class SBSGuideSubSectionAdmin(admin.ModelAdmin):
#     inlines = [SBSGuideSubSectionInline]
#     list_display = ('parent_guide', 'sbs_index',)
#     list_filter = ('sub_headings_and_contents',)
#     # exclude = ('paragraphs', 'step_by_step_guide',)


# class BlogSBSGuideInline(admin.TabularInline):
#     model = BlogStepByStepGuide
#     extra = 1


class ParagraphsInline(admin.TabularInline):
    model = BlogParagraph
    extra = 1


class BlogStepByStepGuideInline(admin.TabularInline):
    model = BlogStepByStepGuide
    extra = 1


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    inlines = [ParagraphsInline]
    list_display = ('title', 'slug', 'cover_image',)
    # list_filter = ('step_by_step_guide',)
    exclude = ('paragraphs', 'step_by_step_guides')


@admin.register(BlogParagraph)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = (
        'paragraph_title', 'paragraph_content',)
    inlines = [BlogStepByStepGuideInline, ParagraphsInline]


@admin.register(BlogStepByStepGuide)
class BlogStepByStepGuideAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'sbs_guide_number',
                    'sbs_index',)
    list_filter = ('blog_post', 'sbs_guide_number')
    exclude = ('sbs_self_refer',)
    inlines = [BlogStepByStepGuideInline]


# @admin.register(SubFields)
# class SubFieldsAdmin(admin.ModelAdmin):
#     list_display = ('sbs_guide_sub_section', 'sub_heading')
#     list_filter = ('sbs_guide_sub_section__blog_post',
#                    'sbs_guide_sub_section__sbs_guide_number')


admin.site.register(Category)
admin.site.register(BlogPostImage)
# admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Reply)
# admin.site.register(BlogParagraph)
# admin.site.register(BlogStepByStepGuide)
admin.site.register(TopicType)
