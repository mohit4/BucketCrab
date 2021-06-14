from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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

    start_date = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buckets')

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("buckets:bucket-detail", kwargs={"pk":self.pk})


class Task(TimeStampedModel):
    """
    A task can be placed into a bucket.
    Activities can be logged onto tasks.
    """
    title = models.CharField(max_length=100, help_text='Summary of the task')
    totalItems = models.PositiveIntegerField(default=0)
    completedItems = models.PositiveIntegerField(default=0)
    progress = models.PositiveIntegerField(default=0)

    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("buckets:bucket-detail", kwargs={"pk":self.bucket.pk})


class Activity(TimeStampedModel):
    """
    A single activity that can be added to a task
    """
    text = models.TextField(help_text='Enter details of the activities performed')

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='activities')

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse("buckets:task-detail", kwargs={"pk":self.task.pk})


class CheckListItem(TimeStampedModel):
    """
    A check list item is a single item from the check-list
    """
    text = models.CharField(max_length=100, help_text='Enter details of check list item')
    is_completed = models.BooleanField(default=False)

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='checklistitems')

    def __str__(self):
        result = "completed" if self.is_completed else "not completed"
        return f"{result} : {self.text}"
    
    def get_absolute_url(self):
        return reverse("buckets:task-detail", kwargs={"pk":self.task.pk})
