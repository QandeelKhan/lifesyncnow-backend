from django.db import models
from django.conf import settings


class TermsAndConditions(models.Model):
    """
    Model representing the terms and conditions of the website.
    """
    title = models.CharField(
        max_length=255, help_text='The title of the terms and conditions.')
    content = models.TextField(
        help_text='The content of the terms and conditions.')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Terms and Conditions'

    def __str__(self):
        return self.title


class Clause(models.Model):
    """
    Model representing a clause within the terms and conditions.
    """
    terms_and_conditions = models.ForeignKey(
        TermsAndConditions, on_delete=models.CASCADE, related_name='clauses')
    clue_title = models.CharField(
        max_length=255, help_text='The title of the clause.')
    clue_content = models.TextField(help_text='The content of the clause.')
    order = models.PositiveIntegerField(
        help_text='The order in which the clause should appear in the terms and conditions.')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.clue_title


class UserAgreement(models.Model):
    """
    Model representing a user's agreement to the terms and conditions.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_agreements', help_text="The user of agreement.")
    terms_and_conditions = models.ForeignKey(
        TermsAndConditions, on_delete=models.CASCADE, related_name='user_agreements')
    agreed_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'User Agreements'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} agreed to {self.terms_and_conditions.title} on {self.agreed_date}"
