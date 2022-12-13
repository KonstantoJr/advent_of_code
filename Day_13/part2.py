class Wrapper:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return isInOrder(self.value, other.value)

    def __gt__(self, other):
        return not isInOrder(self.value, other.value)

    def __eq__(self, other):
        return self.value == other

    def __repr__(self):
        return f'Wrapper({self.value})'


def isInOrder(packet1, packet2):
    if type(packet1) == type(packet2) == type(1):
        if packet1 == packet2:
            return None
        return packet1 < packet2
    if type(packet1) == type(1):
        packet1 = [packet1]
    if type(packet2) == type(1):
        packet2 = [packet2]

    for i, j in zip(packet1, packet2):
        packet = isInOrder(i, j)
        if packet is not None:
            return packet
    if len(packet1) < len(packet2):
        return True
    if len(packet1) > len(packet2):
        return False
    return None


with open('input.txt', 'r') as f:
    pairs = []
    data = f.read().split('\n\n')
    for packets in data:
        pair = []
        for packet in packets.splitlines():
            pair.append(eval(packet.strip()))
        pairs.append(tuple(pair))
    packets = [Wrapper([2]), Wrapper([6])]
    for p in pairs:
        for i in p:
            packets.append(Wrapper(i))
    packets.sort()
    print((packets.index([2]) + 1) * (packets.index([6]) + 1))
