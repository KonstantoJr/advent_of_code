package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func createDirectionMap(graph [][]string) map[Node][]Node {
	// Create a map to store the neighbors of each node
	directionMap := make(map[Node][]Node)
	// Iterate over the graph
	for i := 0; i < len(graph); i++ {
		for j := 0; j < len(graph[i]); j++ {
			// Create a node
			value, err := strconv.Atoi(graph[i][j])
			// Check for errors
			if err != nil {
				log.Fatal(err)
			}
			node := Node{Coords{i, j}, value}
			// Get the neighbors of the node
			neighbors := node.Neighbors(graph)
			// Add the neighbors to the map
			directionMap[node] = neighbors
		}
	}
	// Return the map
	return directionMap
}

func BFS(directionMap map[Node][]Node, start Coords, part2 bool) int {
	// Create a map to store the visited cells
	visited := make(CoordsSet)
	// Create a queue to store the nodes to visit
	queue := []Node{{start, 0}}
	result := 0
	// Iterate over the queue
	for len(queue) > 0 {
		// Get the first node
		node := queue[0]
		// Remove the first node from the queue
		queue = queue[1:]
		// Check if the node has been visited
		if visited.Contains(node.Coords) && !part2 {
			continue
		}
		// Mark the node as visited
		if node.Value == 9 && (!visited.Contains(node.Coords) || part2) {
			result++
		}
		visited.Add(node.Coords)
		// Get the neighbors of the node
		neighbors := directionMap[node]
		// Add the neighbors to the queue

		queue = append(queue, neighbors...)
	}
	return result
}

func readInput(file string) [][]string {
	// Read the input file
	input, err := os.ReadFile(file)
	// Check for errors
	if err != nil {
		log.Fatal(err)
	}

	// Read the input file
	scanner := bufio.NewScanner(strings.NewReader(string(input)))
	// Create a slice to store the input
	var inputSlice [][]string
	// Iterate over the lines
	for scanner.Scan() {
		// Append the line to the slice
		inputSlice = append(inputSlice, strings.Split(scanner.Text(), ""))
	}
	// Return the slice
	return inputSlice
}

func findTrailHeads(input [][]string) CoordsSet {
	// Create a map to store the trail heads
	trailHeads := make(CoordsSet)
	// Iterate over the input
	for i := 0; i < len(input); i++ {
		for j := 0; j < len(input[i]); j++ {
			if input[i][j] == "0" {
				trailHeads.Add(Coords{i, j})
			}
		}
	}
	// Return the trail heads
	return trailHeads
}

func part1() int {
	// Read the input
	input := readInput("input.txt")
	trailHeads := findTrailHeads(input)
	directionMap := createDirectionMap(input)
	result := 0

	for trailHead := range trailHeads {
		result += BFS(directionMap, trailHead, false)
	}

	// Return the result
	return result
}

func part2() int {
	// Read the input
	input := readInput("input.txt")
	trailHeads := findTrailHeads(input)
	directionMap := createDirectionMap(input)
	result := 0

	for trailHead := range trailHeads {
		result += BFS(directionMap, trailHead, true)
	}

	// Return the result
	return result
}

func main() {
	// Print the result
	log.Println(part1())
	log.Println(part2())
}
