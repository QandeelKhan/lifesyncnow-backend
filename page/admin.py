from django.contrib import admin
from .models import ContactUs, AdvertiseWithWellPlusGood, PrivacyPolicy
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


class ContactUsAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        model = ContactUs
        fields = '__all__'


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    form = ContactUsAdminForm
    list_display = ('title', 'content',)
    exclude = ('paragraphs_self_refer',)


class AdvertiseWithWellPlusGoodAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(config_name='default'))

    class Meta:
        model = AdvertiseWithWellPlusGood
        fields = '__all__'


@admin.register(AdvertiseWithWellPlusGood)
class AdvertiseWithWellPlusGood(admin.ModelAdmin):
    form = AdvertiseWithWellPlusGoodAdminForm
