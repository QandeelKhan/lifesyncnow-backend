from django.contrib import admin
from .models import ContactUs, Paragraph, AdvertiseWithWellPlusGood, PrivacyPolicy
from .paragraph_with_sbs import StepByStepGuide, Paragraph


class StepByStepGuideInline(admin.TabularInline):
    model = StepByStepGuide
    extra = 1


# @admin.register(SBSGuideSubSection)
# class SBSGuideSubSectionAdmin(admin.ModelAdmin):
#     inlines = [SBSGuideSubSectionInline]
#     list_display = ('parent_guide', 'sbs_index',)
#     list_filter = ('sub_headings_and_contents',)
    # exclude = ('paragraphs', 'step_by_step_guide',)


# class ContactUsSBSGuideInline(admin.TabularInline):
#     model = StepByStepGuid
#     extra = 1


class ParagraphsInline(admin.TabularInline):
    model = Paragraph
    extra = 1


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    inlines = [ParagraphsInline]
    list_display = ('title', 'content',)
    # list_filter = ('step_by_step_guide',)
    exclude = ('paragraphs_self_refer', 'paragraphs',)


@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = (
        'paragraph_title', 'paragraph_content',)
    exclude = ('step_by_step_guide', 'paragraphs_self_refer',)
    inlines = [StepByStepGuideInline]


@admin.register(StepByStepGuide)
class BlogStepByStepGuideAdmin(admin.ModelAdmin):
    list_display = ('sbs_guide_number',
                    'sbs_index',)
    # list_filter = ('contact_us', 'sbs_guide_number')
    exclude = ('sbs_self_refer',)
    # inlines = [StepByStepGuideInline]


# admin.site.register(StepByStepGuide)
admin.site.register(AdvertiseWithWellPlusGood)
admin.site.register(PrivacyPolicy)
