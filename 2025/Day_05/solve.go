package main

import (
	"fmt"
	"os"
	"slices"
	"strings"
)

type Range struct {
	start uint64
	end   uint64
}

func readInputFile(filename string) ([]uint64, []Range, error) {
	data, err := os.ReadFile(filename)
	if err != nil {
		return nil, nil, err
	}

	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	var ranges []Range
	var ids []uint64
	idsPart := false
	for _, line := range lines {
		if line == "" {
			idsPart = true
			continue
		}
		if !idsPart {
			line := strings.Split(line, "-")
			var start, end uint64
			fmt.Sscanf(line[0], "%d", &start)
			fmt.Sscanf(line[1], "%d", &end)
			ranges = append(ranges, Range{start: start, end: end})
		} else {
			var id uint64
			fmt.Sscanf(line, "%d", &id)
			ids = append(ids, id)
		}
	}

	return ids, ranges, nil
}

func part1(ids []uint64, ranges []Range) int {
	ans := 0
	for _, id := range ids {
		for _, r := range ranges {
			if id >= r.start && id <= r.end {
				ans++
				break
			}
		}
	}
	return ans
}
func part2(ranges []Range) uint64 {
	var ans uint64 = 0

	slices.SortFunc(ranges, func(a, b Range) int {
		if a.start < b.start {
			return -1
		} else if a.start > b.start {
			return 1
		} else {
			return 0
		}
	})

	for i, r := range ranges {
		start := r.start
		end := r.end
		overlapped := false
		for j := range i {
			if start >= ranges[j].start && start <= ranges[j].end {
				if end <= ranges[j].end {
					overlapped = true
					break
				} else {
					start = ranges[j].end + 1
				}
			}
			if end >= ranges[j].start && end <= ranges[j].end {
				if start >= ranges[j].start {
					overlapped = true
					break
				} else {
					end = ranges[j].start - 1
				}
			}
		}
		if overlapped {
			continue
		}
		ans += end - start + 1
	}

	return ans
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run solve.go <inputfile>")
		return
	}

	filename := os.Args[1]
	ids, ranges, err := readInputFile(filename)

	if err != nil {
		fmt.Printf("Error reading input file: %v\n", err)
		return
	}

	fmt.Println("Part 1:", part1(ids, ranges))
	fmt.Println("Part 2:", part2(ranges))

}
