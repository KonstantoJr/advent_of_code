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
    inOrder = []
    for i, p in enumerate(pairs, 1):
        if isInOrder(p[0], p[1]):
            inOrder.append(i)
    print(sum(inOrder))
