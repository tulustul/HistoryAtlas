from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .map_reader import get_cell_data, Timerange
from .models import Cell
from .serializers import MapEntitySerializer


@api_view(['GET'])
def map_view(request: Request) -> Response:
    cell = Cell(
        x=request.QUERY_PARAMS.get('x'),
        y=request.QUERY_PARAMS.get('y'),
        lod=request.QUERY_PARAMS.get('l'),
    )

    timerange = Timerange(
      start=request.QUERY_PARAMS.get('s'),
      end=request.QUERY_PARAMS.get('e'),
    )

    if not cell.is_valid:
        return Response('Incorrect cell definition', 400)

    if not timerange.end:
        return Response('Missing end time', 400)

    map_entities = get_cell_data(cell, timerange)

    serializer = MapEntitySerializer(map_entities, many=True)

    return Response(serializer.data)
