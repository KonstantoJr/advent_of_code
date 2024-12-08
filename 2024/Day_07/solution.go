package main

import (
	"bufio"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

func calculateEquationPart2(target int64, numbers []int64) bool {
	// operators  + * ||
	// all equations are evaluated from left to right
	// no precedence

	for i := 0; i < int(math.Pow(3, float64(len(numbers)-1))); i++ {
		// convert i to binary
		binary := strconv.FormatInt(int64(i), 3)
		// pad with zeros
		for len(binary) < len(numbers)-1 {
			binary = "0" + binary
		}

		// calculate the equation
		equation := numbers[0]
		for j := 0; j < len(binary); j++ {
			if binary[j] == '0' {
				equation += numbers[j+1]
			} else if binary[j] == '1' {
				equation *= numbers[j+1]
			} else {
				// If we have 2 we need to concatenate the the equation with the next number
				equationStr := strconv.FormatInt(equation, 10)
				equationStr += strconv.FormatInt(numbers[j+1], 10)
				equationS, err := strconv.ParseInt(equationStr, 10, 64)
				if err != nil {
					log.Fatal(err)
				}
				equation = equationS
			}
		}

		if equation == target {
			return true
		}
	}
	return false
}

func calculateEquationPart1(target int64, numbers []int64) bool {
	// operators  + *
	// all equations are evaluated from left to right
	// no precedence

	for i := 0; i < int(math.Pow(2, float64(len(numbers)-1))); i++ {
		// convert i to binary
		binary := strconv.FormatInt(int64(i), 2)
		// pad with zeros
		for len(binary) < len(numbers)-1 {
			binary = "0" + binary
		}

		// calculate the equation
		equation := numbers[0]
		for j := 0; j < len(binary); j++ {
			if binary[j] == '0' {
				equation += numbers[j+1]
			} else {
				equation *= numbers[j+1]
			}
		}

		if equation == target {
			return true
		}
	}
	return false
}

func main() {
	f, err := os.Open("input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)
	var part1 int64 = 0
	var part2 int64 = 0
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " ")
		// the first string removing the last character is the target and the
		// rest are the numbers
		target, err := strconv.ParseInt(line[0][:len(line[0])-1], 10, 64)
		if err != nil {
			log.Fatal(err)
		}

		numbers := make([]int64, len(line)-1)
		for i := 1; i < len(line); i++ {
			numbers[i-1], err = strconv.ParseInt(line[i], 10, 64)
			if err != nil {
				log.Fatal(err)
			}
		}

		if calculateEquationPart1(target, numbers) {
			part1 += target
		}

		if calculateEquationPart2(target, numbers) {
			part2 += target
		}

	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	log.Println(part1)
	log.Println(part2)
}
