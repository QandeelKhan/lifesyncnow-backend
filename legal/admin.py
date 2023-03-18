from django.contrib import admin
from .models import TermsAndConditions, Clause, UserAgreement


class ClauseInline(admin.TabularInline):
    model = Clause
    extra = 1


@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    inlines = [ClauseInline]
    list_display = ('title', 'content', 'date_created', 'date_updated')


@admin.register(UserAgreement)
class UserAgreementAdmin(admin.ModelAdmin):
    list_display = ('user', 'terms_and_conditions', 'agreed_date')


@admin.register(Clause)
class ClauseAdmin(admin.ModelAdmin):
    list_display = (
        'clue_title', 'clue_content', 'terms_and_conditions', 'order')
