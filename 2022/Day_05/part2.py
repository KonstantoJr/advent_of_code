with open('input.txt', 'r') as f:
    stacks = [[] for _ in range(9)]
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
                temp = temp[::-1]
                stacks[i] = temp
                # print(temp)
            count += 1
        elif count >= 9:
            if "move" in line:
                temp = line.strip().split(" ")
                how = temp[1]
                fromStack = temp[3]
                toStack = temp[5]

                if len(stacks[int(fromStack) - 1]) != 0:
                    if len(stacks[int(fromStack) - 1]) >= int(how):
                        # print(how, fromStack, toStack)
                        # print(stacks[int(fromStack) - 1])
                        # print(stacks[int(toStack) - 1])
                        item = stacks[int(fromStack) - 1][-1:-(int(how)+1):-1]
                        for _ in range(int(how)):
                            stacks[int(fromStack)-1].pop()
                        stacks[int(toStack) - 1].extend(item[::-1])
                        # print(item)
                        # print(stacks[int(toStack) - 1])
                        # print(stacks[int(fromStack) - 1])
                    else:
                        item = stacks[int(fromStack) - 1][::]
                        stacks[int(toStack) - 1].extend(item)
                        stacks[int(fromStack) - 1] = []
    ans = ""
    for i in stacks:
        if i != []:
            ans += i.pop()
        else:
            ans += " "
    ans = ans.replace("[", "")
    ans = ans.replace("]", "")
    print(ans)
