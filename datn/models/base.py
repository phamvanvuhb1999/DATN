from django.db import models
from django_softdelete.models import SoftDeleteModel  # noqa


class TimeStampModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    modified_time = models.DateTimeField(auto_now=True, editable=True, null=True, blank=True)

    class Meta:
        abstract = True
