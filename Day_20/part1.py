class Node:
    def __init__(self, value):
        self.value = value


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

encrypted = []
for i in data:
    encrypted.append(Node(int(i)))

decrypted = encrypted.copy()

for node in encrypted:
    numberIndex = decrypted.index(node)
    decrypted.remove(node)
    newIndex = (numberIndex + node.value) % len(decrypted)
    if newIndex == 0:
        newIndex = len(decrypted)
    decrypted.insert(newIndex, node)

for node in decrypted:
    if node.value == 0:
        zeroIndex = decrypted.index(node)
        break


first = (decrypted[(zeroIndex + 1000) % len(decrypted)].value)
second = (decrypted[(zeroIndex + 2000) % len(decrypted)].value)
third = (decrypted[(zeroIndex + 3000) % len(decrypted)].value)
print(first + second + third)
