package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Ranges struct {
	start int
	end   int
}

func readInput(filePath string) ([]Ranges, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return nil, err
	}
	lines := strings.Split(strings.TrimSpace(string(data)), ",")
	ranges := make([]Ranges, len(lines))
	for i, line := range lines {
		pairs := strings.Split(line, "-")
		start, err := strconv.Atoi(pairs[0])
		if err != nil {
			return nil, err
		}
		end, err := strconv.Atoi(pairs[1])
		if err != nil {
			return nil, err
		}
		ranges[i] = Ranges{start: start, end: end}
	}
	return ranges, nil
}

func part1(ranges []Ranges) int {
	count := 0

	for _, r := range ranges {
		for i := r.start; i <= r.end; i++ {
			str := strconv.Itoa(i)
			if len(str)%2 != 0 {
				continue
			}
			firstHalf := str[:len(str)/2]
			secondHalf := str[len(str)/2:]
			if firstHalf == secondHalf {
				count += i
			}
		}
	}
	return count
}

func part2(ranges []Ranges) int {
	count := 0

	for _, r := range ranges {
		for i := r.start; i <= r.end; i++ {
			str := strconv.Itoa(i)
			for j := 0; j < len(str)/2; j++ {
				pattern := str[:j+1]
				repeated := strings.Repeat(pattern, len(str)/(j+1))
				if repeated == str {
					count += i
					break
				}
			}
		}
	}
	return count
}

func main() {
	if len(os.Args) < 1 {
		fmt.Println("Provide input file")
		return
	}
	inputFile := os.Args[1]
	ranges, err := readInput(inputFile)
	if err != nil {
		fmt.Println("Error reading input:", err)
		return
	}
	fmt.Println("Part 1 Result:", part1(ranges))
	fmt.Println("Part 2 Result:", part2(ranges))
}
