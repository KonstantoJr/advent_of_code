package main

import (
	"log"
	"strconv"
)

type Node struct {
	// The coordinates of the node
	Coords Coords
	Value  int
}

func (n Node) Neighbors(graph [][]string) []Node {

	// Create a slice to store the neighbors
	neighbors := []Node{}
	// Create a slice to store the directions
	directions := []Coords{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	// Iterate over the directions
	for _, dir := range directions {
		// Calculate the coordinates of the neighbor
		neighborCoords := Coords{n.Coords.x + dir.x, n.Coords.y + dir.y}
		// Check if the neighbor is inside the graph
		if neighborCoords.x >= 0 && neighborCoords.x < len(graph) && neighborCoords.y >= 0 && neighborCoords.y < len(graph[0]) {
			// If the neighbor value is not one higher than the current node value, skip it
			// Parse the neighbor value
			neighborValue, err := strconv.Atoi(graph[neighborCoords.x][neighborCoords.y])
			// Check for errors
			if err != nil {
				log.Fatal(err)
			}
			// If the neighbor value is not one higher than the current node value, skip it
			if neighborValue != n.Value+1 {
				continue
			}
			// Create a new node
			neighbor := Node{neighborCoords, neighborValue}
			// Append the neighbor to the slice
			neighbors = append(neighbors, neighbor)

		}
	}
	// Return the neighbors
	return neighbors
}
