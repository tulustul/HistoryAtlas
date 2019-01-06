from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from rest_framework.fields import JSONField


class Changeset(models.Model):

    protocol_version: int = models.IntegerField()

    author: User = models.ForeignKey(User, on_delete=models.CASCADE)

    created: datetime = models.DateTimeField(auto_now_add=True)


class Change(models.Model):

    raw_data = JSONField()

    changeset = models.ForeignKey(Changeset, on_delete=models.CASCADE)
