from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import YashasBlogPost, YashasComment
import time
import threading

@receiver(post_save, sender=YashasBlogPost)
def slow_notify_yashas(sender, instance, created, **kwargs):
    if created and instance.author.lower() == "yashas":
        current_thread = threading.current_thread()
        print(f"Notification to Yashas starting at {time.time()} in thread: {current_thread.name} (ID: {current_thread.ident})")
        time.sleep(2)  # Simulate a time-consuming operation
        print(f"Notification to Yashas finished at {time.time()} in thread: {current_thread.name}")

@receiver(post_save, sender=YashasBlogPost)
def create_yashas_welcome_comment(sender, instance, created, **kwargs):
    if created:
        YashasComment.objects.create(post=instance, content=f"Welcome to your new blog post, {instance.author}!")
        print(f"Created welcome comment for {instance.author}'s post: {instance.title}")
