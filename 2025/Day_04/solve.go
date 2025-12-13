package main

import (
	"fmt"
	"os"
	"strings"
)

func readInputFile(input string) [][]string {
	data, err := os.ReadFile(input)
	if err != nil {
		panic(err)
	}
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	grid := make([][]string, len(lines))
	for i, line := range lines {
		grid[i] = strings.Split(line, "")
	}
	return grid

}

func part1(grid [][]string) int {
	ans := 0
	directions := []struct{ dx, dy int }{
		{1, 0},   // right
		{0, 1},   // down
		{-1, 0},  // left
		{0, -1},  // up
		{1, 1},   // down-right
		{-1, 1},  // down-left
		{-1, -1}, // up-left
		{1, -1},  // up-right
	}
	for i := range grid {
		for j := range grid[i] {
			rolls := 0
			if grid[i][j] == "." {
				continue
			}
			for _, dir := range directions {
				x, y := i+dir.dx, j+dir.dy
				if x >= 0 && x < len(grid) && y >= 0 && y < len(grid[i]) && grid[x][y] == "@" {
					rolls++
				}
			}
			if rolls < 4 {
				ans++
			}
		}
	}
	return ans
}

func part2(grid [][]string) int {
	ans := 0
	directions := []struct{ dx, dy int }{
		{1, 0},   // right
		{0, 1},   // down
		{-1, 0},  // left
		{0, -1},  // up
		{1, 1},   // down-right
		{-1, 1},  // down-left
		{-1, -1}, // up-left
		{1, -1},  // up-right
	}
	for {
		noChanges := true
		for i := range grid {
			for j := range grid[i] {
				rolls := 0
				if grid[i][j] == "." {
					continue
				}
				for _, dir := range directions {
					x, y := i+dir.dx, j+dir.dy
					if x >= 0 && x < len(grid) && y >= 0 && y < len(grid[i]) && grid[x][y] == "@" {
						rolls++
					}
				}
				if rolls < 4 {
					ans++
					noChanges = false
					grid[i][j] = "."
				}
			}
		}
		if noChanges {
			break
		}
	}

	return ans
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run solve.go <input>")
		return
	}

	file := os.Args[1]
	grid := readInputFile(file)

	result1 := part1(grid)
	fmt.Println("Part 1:", result1)
	result2 := part2(grid)
	fmt.Println("Part 2:", result2)
}
