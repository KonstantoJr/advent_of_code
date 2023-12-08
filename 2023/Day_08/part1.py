"""Day 8 part 1"""


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
    """Follow the instructions starting from AAA and stop when 
    you reach ZZZ if the instructions end then start again from the 
    instruction at the beginning"""

    # Start from AAA
    current_node = "AAA"
    path = []
    instruction_index = 0
    while True:
        # Get the next instruction
        instruction = instructions[instruction_index]
        # Get the next node
        next_node = nodes[current_node][0] if instruction == "L" else nodes[current_node][1]
        # Add the instruction to the path
        path.append(instruction)
        # If the next node is ZZZ then return the path
        if next_node == "ZZZ":
            return path
        # Otherwise update the current node
        current_node = next_node
        # Increment the instruction index
        instruction_index += 1
        # If the instruction index is equal to the length of the instructions
        # then reset the instruction index
        if instruction_index == len(instructions):
            instruction_index = 0


if __name__ == "__main__":
    INSTRUCTIONS, NODES = input_parse()
    print(len(follow_path(INSTRUCTIONS, NODES)))
