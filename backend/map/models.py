from dataclasses import dataclass
import datetime

from django.db import models
from django.contrib.postgres.fields import JSONField

from entities.models import HistoricEntity


@dataclass
class Cell:
    x: int
    y: int
    lod: int

    def is_valid(self):
        return all(self.x, self.y, self.lod)


class CellTimestampManager(models.Manager):

    def get_cell(self, cell: Cell):
        return self.get(x=cell.x, y=cell.y, lod=cell.lod)


class CellTimestamp(models.Model):

    class Meta:
        unique_together = ('x', 'y', 'lod', 'timestamp')

    objects = CellTimestampManager()

    x: int = models.IntegerField()

    y: int = models.IntegerField()

    lod: int = models.IntegerField()

    timestamp: datetime.datetime = models.DateTimeField()

    is_keyframe: bool = models.BooleanField(default=False)


class MapEntity(models.Model):

    layer: str = models.CharField(max_length=32)

    data: dict = JSONField()

    entity: HistoricEntity = models.ForeignKey(
        HistoricEntity,
        on_delete=models.CASCADE,
        related_name='map_entities',
    )

    cell: CellTimestamp = models.ForeignKey(
        CellTimestamp,
        on_delete=models.CASCADE,
        related_name='map_entities',
    )
