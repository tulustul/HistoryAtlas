from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import math
from typing import List

from .models import CellTimestamp


@dataclass
class Timerange:
    start: datetime
    end: datetime


def get_cell_data(cell: Cell, timerange: Timerange) -> List[MapEntity]:
    keyframe = _get_keyframe_for(cell, timerange.end)

    if not keyframe:
        return []

    keyframe_data = None
    if not timerange.start or keyframe.timestamp > timerange.start:
        keyframe_data = keyframe.map_entities.all()
        timerange.start = keyframe.timestamp

    changes_data = _get_map_changes(cell, timerange)

    if keyframe_data:
        return _merge_map_changes(keyframe_data, changes_data)
    else:
        return changes_data


def _get_map_changes(cell: Cell, timerange: Timerange) -> List[MapEntity]:
    sorting_prefix = '-' if timerange.start > timerange.end else ''
    cell_timestamps = CellTimestamp.objects
        .get_cell(cell)
        .filter(
            timestamp__ge=min(timerange.start, timerange.end),
            timestamp__le=max(timerange.start, timerange.end),
        )
        .order_by(f'{sorting_prefix}timestamp').prefetch_related('map_entities')

    changes = []
    for cell in cell_timestamps:
        changes = _merge_map_changes(changes, cell.map_entities.all())

    return changes


def _merge_map_changes(target: List[MapEntity], source: List[MapEntity]):
    entities_map = {entity.id: index for index, entity in enumerate(target)}
    for entity in source:
        index = entities_map.get(entity.id)
        if index:
            target[index] = entity
        else:
            target.append(entity)
    return target


def _get_keyframe_for(cell: Cell, timestamp: datetime) -> CellTimestamp:
    return CellTimestamp.objects
        .get_cell(cell)
        .filter(is_keyframe=True, timestamp__le=timestamp)
        .order_by('-timestamp')
        .first()
