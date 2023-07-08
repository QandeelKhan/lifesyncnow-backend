from django.contrib import admin
from .models import SEO
# Register your models here.


class SEOInline(admin.TabularInline):
    model = SEO


@admin.register(SEO)
class SEOAdmin(admin.ModelAdmin):
    pass
