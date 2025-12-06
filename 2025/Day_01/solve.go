// AOC Day 1 - 2025

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// Read Input file
// Return a list with an object that has a command and a value
type Instruction struct {
	Command string
	Value   int64
}

func readInputFile(filePath string) ([]Instruction, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var instructions []Instruction
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		var command = string(line[0])
		var value, _ = strconv.ParseInt(line[1:], 10, 64)
		instructions = append(instructions, Instruction{Command: command, Value: value})
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return instructions, nil
}

func part1(instructions []Instruction) {
	pos := int64(50)
	// Range 0 - 99
	ans := int64(0)
	for _, instr := range instructions {
		switch instr.Command {
		case "L":
			clockwise := instr.Value % 100
			pos = (pos - clockwise + 100) % 100
		case "R":
			clockwise := instr.Value % 100
			pos = (pos + clockwise) % 100
		}
		if pos == 0 {
			ans += 1
		}
	}
	fmt.Println("Part 1 Answer:", ans)

}

func part2(instructions []Instruction) {
	pos := int64(50)
	ans := int64(0)

	for _, instr := range instructions {
		switch instr.Command {
		case "L":
			full_turns := instr.Value / 100
			ans += full_turns
			clockwise := instr.Value % 100
			new_pos := (pos - clockwise + 100) % 100
			if new_pos > pos {
				ans += 1
			}
			pos = new_pos
		case "R":
			full_turns := instr.Value / 100
			ans += full_turns
			clockwise := instr.Value % 100
			new_pos := (pos + clockwise) % 100
			if new_pos < pos {
				ans += 1
			}
			pos = new_pos
		}
		println(pos)
	}
	fmt.Println("Part 2 Answer:", ans)

}

func main() {
	instructions, err := readInputFile("test.txt")
	if err != nil {
		fmt.Println("Error reading input file:", err)
		return
	}
	part1(instructions)
	part2(instructions)
}
