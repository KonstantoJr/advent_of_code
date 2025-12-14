package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

func readInputFile(filePath string) ([]string, [][]uint64, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return nil, nil, err
	}
	var operators []string
	var numbers [][]uint64
	lines := strings.Split(string(data), "\n")
	for i, line := range lines {
		if i == len(lines)-1 {
			// Last line contains operators
			line = strings.TrimSpace(line)
			if line != "" {
				line = strings.ReplaceAll(line, " ", "")
				operators = append(operators, strings.Split(line, "")...)
			}
			break
		}
		line = strings.TrimSpace(line)
		if line != "" {
			// write me a regex that finds all the numbers in the line
			re := regexp.MustCompile(`\d+`)
			nums := re.FindAllString(line, -1)
			var tempNumbers []uint64
			for _, num := range nums {
				var n uint64
				fmt.Sscanf(num, "%d", &n)
				tempNumbers = append(tempNumbers, n)
			}
			numbers = append(numbers, tempNumbers)
		}

	}
	return operators, numbers, nil
}

func part1(operators []string, numbers [][]uint64) uint64 {
	var ans uint64 = 0
	length := len(operators)
	for i := range length {
		op := operators[i]
		var temp uint64 = 0
		if op == "*" {
			temp = 1
		}
		for j := range numbers {
			num := numbers[j][i]
			if op == "+" {
				temp += num
			} else if op == "*" {
				temp *= num
			}
		}
		ans += temp
	}

	return ans
}

func readInputFilePart2(filePath string) ([]string, [][]uint64, error) {

	return nil, nil, nil
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run solve.go <input_file_path>")
		return
	}

	inputFilePath := os.Args[1]
	operators, numbers, err := readInputFile(inputFilePath)

	if err != nil {
		fmt.Printf("Error reading input file: %v\n", err)
		return
	}

	fmt.Println("Part 1 Solution:", part1(operators, numbers))
	// Part 2
	operators, numbers, err = readInputFilePart2(inputFilePath)
	if err != nil {
		fmt.Printf("Error reading input file for Part 2: %v\n", err)
		return
	}
	fmt.Println("Part 2 Solution:", part1(operators, numbers))
}
