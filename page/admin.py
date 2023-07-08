from django.contrib import admin
from .models import ContactUs, Paragraph, AdvertiseWithWellPlusGood, PrivacyPolicy
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PrivacyPolicyAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    form = PrivacyPolicyAdminForm


class ParagraphsInline(admin.TabularInline):
    model = Paragraph
    extra = 1


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    inlines = [ParagraphsInline]
    list_display = ('title', 'content',)
    exclude = ('paragraphs_self_refer', 'paragraphs',)


admin.site.register(AdvertiseWithWellPlusGood)
