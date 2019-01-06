import {
  Label,
  Polygon,
  Place,
  MapEntity,
  Line,
} from './map.interface';

const EXAMPLE_CELL: MapEntity[] = [
  {
    type: 'label',
    id: '1',
    text: 'Poland',
    point: [50, 50],
    rot: 0.1,
    size: 20,
    bend: 0.05,
  } as Label,
  {
    type: 'place',
    id: '2',
    point: [49, 50],
    text: 'Wrocław',
  } as Place,
  {
    type: "polygon",
    id: '1',
    points: [],
  } as Polygon,
  {
    type: "line",
    id: '3',
    points: [],
  } as Line,
  {
    type: 'label',
    id: '13',
    text: 'Odra',
    point: [],
    rot: 0.9,
    size: 12,
    bend: 0,
  } as Label,

];