package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readInput(filePath string) ([]string, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return nil, err
	}

	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	numbers := make([]string, len(lines))
	for i, line := range lines {
		numbers[i] = strings.TrimSpace(line)
	}
	return numbers, nil
}
func part1(numbers []string) int {
	count := 0
	for _, number := range numbers {
		digits := strings.Split(number, "")
		max := 0
		for i := range digits {
			for j := i + 1; j < len(digits); j++ {
				num, err := strconv.Atoi(digits[i] + digits[j])
				if err != nil {
					continue
				}
				if num > max {
					max = num
				}
			}
		}
		count += max
	}
	return count
}

func part2(numbers []string) int {
	count := 0
	for _, number := range numbers {
		digits := strings.Split(number, "")
		var ans strings.Builder
		for i := range 12 {
			max := 0
			index := -1
			for j, d := range digits {
				d, err := strconv.Atoi(d)
				if err != nil {
					continue
				}
				if d > max {
					remaining := len(digits) - j - 1
					if remaining >= 12-i-1 {
						max = d
						index = j
					}
				}
			}
			digits = digits[index+1:]
			ans.WriteString(strconv.Itoa(max))
		}
		num, err := strconv.Atoi(ans.String())
		if err != nil {
			continue
		}
		count += num

	}
	return count
}

func main() {
	if len(os.Args) < 1 {
		fmt.Println("Please provide an input file.")
		return
	}
	inputFile := os.Args[1]
	numbers, err := readInput(inputFile)
	if err != nil {
		fmt.Println("Error reading input file:", err)
		return
	}

	resultPart1 := part1(numbers)
	fmt.Println("Part 1 Result:", resultPart1)
	resultPart2 := part2(numbers)
	fmt.Println("Part 2 Result:", resultPart2)
}
