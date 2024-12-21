package main

type Coords struct {
	x int
	y int
}

type CoordsSet map[Coords]struct{}

func (cs CoordsSet) Add(c Coords) {
	cs[c] = struct{}{}
}

func (cs CoordsSet) Contains(c Coords) bool {
	_, ok := cs[c]
	return ok
}

func (cs CoordsSet) Remove(c Coords) {
	delete(cs, c)
}

func (cs CoordsSet) Size() int {
	return len(cs)
}
