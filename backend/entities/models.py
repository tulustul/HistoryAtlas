from django.db import models


class HistoricEntity(models.Model):

    type = models.CharField(max_length=32)

    name = models.CharField(max_length=255)


class Event(models.Model):

    timestamp = models.DateTimeField()

    name = models.CharField(max_length=255)

    related_entities = models.ManyToManyField(
        HistoricEntity,
        related_name='events',
    )
