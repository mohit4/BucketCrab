from django.db import models
from django.urls import reverse


class TimeStampedModel(models.Model):
    """
    Abstract model with ``created`` and ``modified`` time stamps
    """
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Bucket(TimeStampedModel):
    """
    Bucket is equivalent to a project that can contain crab eggs or tasks
    Upon completion, a crab egg is matured into a crab.
    """
    title = models.CharField(max_length=100, help_text='Name of the bucket')
    description = models.TextField(null=True, blank=True, help_text='Few words about the bucket')

    is_open = models.BooleanField(default=True)
    is_expirable = models.BooleanField(default=False)

    expiration_date = models.DateTimeField(null=True, blank=True, help_text='Bucket will be automatically closed on this date')

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("buckets:bucket-detail", kwargs={"pk":self.pk})
