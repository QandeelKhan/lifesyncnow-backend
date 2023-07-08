# blog/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpRequest
from blog.models import BlogPost, View


@receiver(post_save, sender=BlogPost)
def update_earnings(sender, instance, created, **kwargs):
    if created:
        request = kwargs.get('request')
        if isinstance(request, HttpRequest):
            user_ip = request.META.get('REMOTE_ADDR')
            author = instance.author

            # Check if the IP address has already earned from this post
            if not View.objects.filter(blog_post=instance, author=author, ip_address=user_ip).exists():
                # Calculate earnings and update the author's earnings field
                earnings = author.author_earnings + 0.01
                author.author_earnings = earnings
                author.save()

                # Record the IP address to avoid duplicate earnings
                View.objects.create(blog_post=instance,
                                    author=author, ip_address=user_ip)
