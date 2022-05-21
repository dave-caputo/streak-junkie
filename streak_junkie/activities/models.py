import uuid

from django.db import models
from django.urls import reverse


class Activity(models.Model):
    """An activity to be tracked."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"[{self.id}] {self.name}"

    def get_absolute_url(self):
        return reverse("activity-detail", kwargs={"pk": self.pk})
