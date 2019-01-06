
export interface MapEntity {
  id: string;
  type: string;
}

export interface Label extends MapEntity {
  type: 'label';
  text: string;
  point: number[];
  size: number;
  rot: number;
  bend: number;
}

export interface Place extends MapEntity {
  type: 'place';
  point: number[];
  text: string;
}

export interface Line extends MapEntity {
  type: 'line';
  points: number[];
}

export interface Polygon extends MapEntity {
  type: 'polygon';
  points: number[];
}
