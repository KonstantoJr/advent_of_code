with open('input.txt', 'r') as f:
    stack1 = []
    stack2 = []
    stack3 = []
    stack4 = []
    stack5 = []
    stack6 = []
    stack7 = []
    stack8 = []
    stack9 = []
    stacks = [stack1, stack2, stack3, stack4,
              stack5, stack6, stack7, stack8, stack9]
    count = 0
    temp = ""
    for line in f:
        if count < 8:
            stack = 0
            for i, char in enumerate(line):
                temp += char
                if i % 4 == 3:
                    stacks[stack].append(temp.strip())
                    stack += 1
                    temp = ""
            stack = 0
            count += 1
        elif count == 8:
            for i in range(9):
                temp = []
                for j in stacks[i]:
                    if j != "":
                        temp.append(j)
                stacks[i] = temp
                print(temp)
            count += 1
        elif count >= 9:
            if "move" in line:
                temp = line.strip().split(" ")
                how = temp[1]
                fromStack = temp[3]
                toStack = temp[5]
                for i in range(int(how)):
                    # print(int(fromStack))
                    if len(stacks[int(fromStack) - 1]) != 0:
                        item = stacks[int(fromStack) - 1].pop(0)
                        stacks[int(toStack) - 1].insert(0, item)
    ans = ""
    for i in stacks:
        ans += i.pop(0)
    ans = ans.replace("[", "")
    ans = ans.replace("]", "")
    print(ans)
