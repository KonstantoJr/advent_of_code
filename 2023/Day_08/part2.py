"""Day 8 part 2"""
import math


def input_parse():
    """Parse input"""
    instructions = ""
    nodes = {}
    with open("input.txt", 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if i == 0:
                instructions = line.strip()
            else:
                if line.strip() == "":
                    continue
                node = line.split('=')[0].strip()
                elements = line.split('=')[1].strip().replace(
                    '(', "").replace(')', "").split(',')
                nodes[node] = (elements[0].strip(), elements[1].strip())
    return instructions, nodes


def follow_path(instructions, nodes):
    """Follow the instructions and end when all the starting nodes end at 
    are at the same time at an ending node"""
    starting_nodes = [node for node in nodes if node[2] == "A"]
    paths = []
    for _, node in enumerate(starting_nodes):
        total_instructions = 0
        instruction_index = 0
        current_node = node
        while True:
            # Get the next instruction
            instruction = instructions[instruction_index]
            # Get the next node
            next_node = nodes[current_node][0] if instruction == "L" else nodes[current_node][1]
            # Add the instruction to the path
            total_instructions += 1
            # If the next node is ZZZ then return the path
            if next_node[2] == "Z":
                paths.append(total_instructions)
                break
            # Otherwise update the current node
            current_node = next_node
            # Increment the instruction index
            instruction_index += 1
            # If the instruction index is equal to the length of the instructions
            # then reset the instruction index
            if instruction_index == len(instructions):
                instruction_index = 0
    return paths


if __name__ == "__main__":
    INSTRUCTIONS, NODES = input_parse()
    PATHS = follow_path(INSTRUCTIONS, NODES)
    print(math.lcm(*PATHS))
