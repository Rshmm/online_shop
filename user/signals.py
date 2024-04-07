from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from user.models import UserProfile

User = get_user_model()

@receiver(post_save , sender=User)
def user_setup_after_singup(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


