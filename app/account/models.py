from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse


class Profile(models.Model):
    """
    A user profile containing all user details
    """

    bio = models.TextField(null=True, help_text="Few words about you...")
    website = models.URLField(null=True, help_text="Your personal website.")

    coins = models.PositiveBigIntegerField(default=100, help_text="Coins for trading from market place.")
    crab_eggs = models.PositiveBigIntegerField(default=5, help_text="Crab eggs are used to plant tasks in Buckets.")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f"{self.user.username} profile"
    
    def get_absolute_url(self):
        return reverse("account:profile-detail", kwargs={"pk":self.pk})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
