package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

type DiskSpace struct {
	start int
	end   int
	id    int
	size  int
}

func readFile(fileLoc string) string {
	file, err := os.Open(fileLoc)
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	return scanner.Text()
}

func expandDiskMap(diskMap string) []string {
	expanded := make([]string, 0)
	for i, char := range diskMap {
		num, err := strconv.Atoi(string(char))
		if err != nil {
			log.Fatal(err)
		}
		if i%2 == 0 {
			id := strconv.Itoa(i / 2)
			for j := 0; j < num; j++ {
				expanded = append(expanded, id)
			}
		} else {
			for j := 0; j < num; j++ {
				expanded = append(expanded, ".")
			}

		}
	}
	return expanded
}

func moveBlocks(expanded []string) []string {
	compressed := make([]string, len(expanded))
	copy(compressed, expanded)
	start := 0
	end := len(compressed) - 1

	for start < end {
		if compressed[start] == "." {
			if compressed[end] != "." {
				compressed[start] = compressed[end]
				compressed[end] = "."
				start++
				end--
			} else {
				end--
			}
		} else {
			start++
		}
	}

	return compressed
}

func checksumCalculation(compressed []string) int64 {
	var checksum int64 = 0
	for i, char := range compressed {
		if char != "." {
			digit, err := strconv.Atoi(char)
			if err != nil {
				log.Fatal(err)
			}
			checksum += int64(digit) * int64(i)
		}
	}
	return checksum
}

func createDiskSpace(diskMap string) []DiskSpace {
	diskSpace := make([]DiskSpace, 0)
	for i, char := range diskMap {
		num, err := strconv.Atoi(string(char))
		if err != nil {
			log.Fatal(err)
		}
		if i == 0 {
			diskSpace = append(diskSpace, DiskSpace{0, num - 1, 0, num})
		} else if i%2 == 0 {
			id := i / 2
			diskSpace = append(diskSpace, DiskSpace{diskSpace[len(diskSpace)-1].end + 1, diskSpace[len(diskSpace)-1].end + num - 1, id, num})
		} else {
			diskSpace = append(diskSpace, DiskSpace{diskSpace[len(diskSpace)-1].end + 1, diskSpace[len(diskSpace)-1].end + num, -1, num})
		}
	}
	return diskSpace
}

func moveFiles(diskSpace []DiskSpace) []DiskSpace {
	newDisk := make([]DiskSpace, len(diskSpace))
	copy(newDisk, diskSpace)
	for file := len(diskSpace) - 1; file >= 0; file-- {
		if diskSpace[file].id != -1 {
			for empty := 0; empty < len(newDisk); empty++ {
				if newDisk[empty].id == -1 && newDisk[empty].size >= diskSpace[file].size {
					newDisk = append(newDisk, DiskSpace{
						newDisk[empty].start,
						newDisk[empty].start + diskSpace[file].size - 1,
						diskSpace[file].id,
						diskSpace[file].size,
					})
					newDisk[file].id = -1
					newDisk[empty].start += diskSpace[file].size
					newDisk[empty].size -= diskSpace[file].size
					break
				}
			}
		}
	}
	return newDisk
}

func checksumCalculationDiskSpace(diskSpace []DiskSpace) int {
	var checksum int = 0
	for _, disk := range diskSpace {
		if disk.id != -1 {
			for j := disk.start; j <= disk.end; j++ {
				checksum += disk.id * j
			}
		}
	}
	return checksum
}

func printDiskSpace(diskSpace []DiskSpace) {
	deepCopy := make([]DiskSpace, len(diskSpace))
	copy(deepCopy, diskSpace)
	sort.Slice(deepCopy, func(i, j int) bool {
		return deepCopy[i].start < deepCopy[j].start
	})
	std := ""
	for _, disk := range deepCopy {
		fmt.Println(disk)
		for i := 0; i < disk.size; i++ {
			if disk.id == -1 {
				std += "."
			} else {
				std += strconv.Itoa(disk.id)
			}
		}
	}
	fmt.Println(std)
}

func part1(diskMap string) int64 {
	expanded := expandDiskMap(diskMap)
	compressed := moveBlocks(expanded)
	checksum := checksumCalculation(compressed)
	return checksum
}

func part2(diskMap string) int {
	diskSpace := createDiskSpace(diskMap)
	printDiskSpace(diskSpace)
	newDisk := moveFiles(diskSpace)
	printDiskSpace(newDisk)
	checksum := checksumCalculationDiskSpace(newDisk)
	return checksum
}

func main() {
	input := readFile("test.txt")
	fmt.Println(part1(input))
	fmt.Println(part2(input))

}
