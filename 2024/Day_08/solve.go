package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type Coords struct {
	x int
	y int
}

type CoordsSet map[Coords]struct{}

func (c CoordsSet) Add(coords Coords) {
	c[coords] = struct{}{}
}

func (c CoordsSet) Contains(coords Coords) bool {
	_, ok := c[coords]
	return ok
}

func (c CoordsSet) Remove(coords Coords) {
	delete(c, coords)
}

func calculateAntenasAntinode(a1 Coords, a2 Coords) Coords {
	offset := getOffset(a1, a2)
	return Coords{a1.x + offset.x, a1.y + offset.y}

}

func getOffset(a1 Coords, a2 Coords) Coords {
	return Coords{a1.x - a2.x, a1.y - a2.y}
}

func main() {
	f, err := os.Open("input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	var m = make(map[string][]Coords)
	var occupied = make(CoordsSet)
	var antinodesCoords = make(CoordsSet)
	var resonateCoords = make(CoordsSet)
	scanner := bufio.NewScanner(f)
	y := 0
	x_len := 0
	// add all the symbols to the map so we have the coordinates of each seat
	for scanner.Scan() {
		x_len = len(scanner.Text())
		line := scanner.Text()
		for x, c := range line {
			if c != '.' {
				m[string(c)] = append(m[string(c)], Coords{x, y})
				occupied.Add(Coords{x, y})
			}
		}
		y++
	}
	gridHeight := y
	gridWidth := x_len

	// calculate the antinodes for each pair of antennas
	for _, antenas := range m {
		for i, a1 := range antenas {
			for j := 0; j < len(antenas); j++ {
				if i == j {
					continue
				}
				antinode := calculateAntenasAntinode(a1, antenas[j])

				if antinode.x >= 0 && antinode.x < gridWidth && antinode.y >= 0 && antinode.y < gridHeight {
					antinodesCoords.Add(antinode)
				}

				offset := getOffset(a1, antenas[j])
				antinode = Coords{a1.x, a1.y}
				for {
					if antinode.x >= 0 && antinode.x < gridWidth && antinode.y >= 0 && antinode.y < gridHeight {
						resonateCoords.Add(antinode)
					} else {
						break
					}
					antinode = Coords{antinode.x + offset.x, antinode.y + offset.y}
				}

			}

		}
	}
	fmt.Println("Part1: ", len(antinodesCoords))
	fmt.Println("Part2: ", len(resonateCoords))
}
