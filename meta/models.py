from django.db import models
# from page.models import PrivacyPolicy


class SEO(models.Model):
    meta_title = models.CharField(max_length=100, blank=True)
    # recommended 150 to 160 chars
    meta_description = models.TextField(max_length=200, blank=True)
    meta_keywords = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.meta_title

    class Meta:
        verbose_name = "seo"
        verbose_name_plural = "seo"
        db_table = "my_seo_table"
