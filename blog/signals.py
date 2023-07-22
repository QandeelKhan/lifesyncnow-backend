# blog/signals.py

from django.core.cache import cache
from .models import BlogPost
from django.db.models.signals import post_save, post_delete
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpRequest
from blog.models import BlogPost, View
from blog.tasks import clear_blogpost_list_cache, clear_blogpost_detail_cache
# from blog.tasks import clear_blogpost_list_cache


@receiver([post_save, post_delete], sender=BlogPost)
def clear_blogpost_list_cache_signal(sender, instance, **kwargs):
    clear_blogpost_list_cache.delay()
    if kwargs.get('created', False):
        clear_blogpost_detail_cache.delay(instance.slug)


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

# With this signal in place, whenever a blog post is created, updated, or deleted, the cache for the blog post list will be cleared automatically.
    # the cache with the key 'blogpost_list' is cleared using cache.delete('blogpost_list'), the key was introduced in BlogPostListView
# the key blogpost_detail_{instance.slug}, introduced and cached in BlogPostDetailView, and here we clearing both of them


# @receiver([post_save, post_delete], sender=BlogPost)
# def clear_blogpost_cache(sender, instance, **kwargs):
#     cache_key_list = 'blogpost_list'
#     cache_key_detail = f'blogpost_detail_{instance.slug}'
#     cache.delete(cache_key_list)
#     cache.delete(cache_key_detail)


# @shared_task
# def clear_blogpost_cache_task(cache_key):
#     cache.delete(cache_key)
