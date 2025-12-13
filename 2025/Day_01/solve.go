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

type Node struct {
	Pos      int64
	Next     *Node
	Previous *Node
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

func createCircularDoublyLinkedList(size int64) *Node {
	var head *Node
	var tail *Node

	for i := int64(0); i < size; i++ {
		newNode := &Node{Pos: i}
		if head == nil {
			head = newNode
			tail = newNode
			newNode.Next = newNode
			newNode.Previous = newNode
		} else {
			newNode.Previous = tail
			newNode.Next = head
			tail.Next = newNode
			head.Previous = newNode
			tail = newNode
		}
	}
	return head
}

func part2(instructions []Instruction) {
	list := createCircularDoublyLinkedList(100)
	for i := int64(0); i < 50; i++ {
		list = list.Next
	}
	current := list
	ans := int64(0)

	for _, instr := range instructions {
		switch instr.Command {
		case "L":
			for i := int64(0); i < instr.Value; i++ {
				current = current.Previous
				if current.Pos == 0 {
					ans += 1
				}
			}
		case "R":
			for i := int64(0); i < instr.Value; i++ {
				current = current.Next
				if current.Pos == 0 {
					ans += 1
				}
			}
		}
	}
	fmt.Println("Part 2 Answer:", ans)

}

func main() {
	args := os.Args[1:]
	if len(args) < 1 {
		fmt.Println("Please provide the input file path as an argument.")
		return
	}
	instructions, err := readInputFile(args[0])
	if err != nil {
		fmt.Println("Error reading input file:", err)
		return
	}
	part1(instructions)
	part2(instructions)
}
