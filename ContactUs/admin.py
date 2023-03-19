from django.contrib import admin
from .models import ContactUs, Paragraph
from .sbs_model import StepByStepGuid, SBSGuideSubSection, SubFields


class SBSGuideSubSectionInline(admin.TabularInline):
    model = SBSGuideSubSection
    extra = 1


@admin.register(SBSGuideSubSection)
class SBSGuideSubSectionAdmin(admin.ModelAdmin):
    inlines = [SBSGuideSubSectionInline]
    list_display = ('parent_guide', 'sbs_index',)
    list_filter = ('sub_headings_and_contents',)
    # exclude = ('paragraphs', 'step_by_step_guide',)


class ContactUsSBSGuideInline(admin.TabularInline):
    model = StepByStepGuid
    extra = 1


class ParagraphsInline(admin.TabularInline):
    model = Paragraph
    extra = 1


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    inlines = [ParagraphsInline, ContactUsSBSGuideInline,
               SBSGuideSubSectionInline]
    list_display = ('title', 'content',)
    list_filter = ('step_by_step_guide',)
    exclude = ('paragraphs', 'step_by_step_guide',)


@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = (
        'paragraph_title', 'paragraph_content',)


admin.site.register(StepByStepGuid)
admin.site.register(SubFields)
