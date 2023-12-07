"""Day 7 part 2"""
ORDER = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
ORDER.reverse()


def input_parse():
    """Parse input file"""
    hands = []
    with open("input.txt", "r", encoding='utf-8') as file:
        for line in file:
            _hand = line.strip().split()[0]
            _bid = line.strip().split()[1]
            hands.append([_hand, _bid, 0])
    return hands


def check_hand_rank(hand):
    """Check hand rank"""
    hand_rank = 0
    hand_set = set(hand)
    # The J is the joker and we need to determine the best rank

    if 'J' in hand_set:
        # Check for five of a kind
        if len(hand_set) == 2 or len(hand_set) == 1:
            hand_rank = 7
        # Check for four of a kind or full house
        elif len(hand_set) == 3:
            for card in hand_set:
                if hand.count(card) == 3:
                    hand_rank = 6
                    break
                if hand.count(card) == 2 and hand.count('J') == 1:
                    hand_rank = 5
                    break
                if hand.count(card) == 2 and hand.count('J') == 2:
                    hand_rank = 6
                    break

        # Check for three of a kind or two pair
        elif len(hand_set) == 4:
            hand_rank = 4
        # Check for one pair
        else:
            hand_rank = 2
        print(hand, hand_rank)
        return hand_rank
    # Check for five of a kind
    if len(hand_set) == 1:
        hand_rank = 7
    # Check for four of a kind or full house
    elif len(hand_set) == 2:
        for card in hand_set:
            if hand.count(card) == 4:
                hand_rank = 6
                break
            elif hand.count(card) == 3:
                hand_rank = 5
                break
    # Check for three of a kind or two pair
    elif len(hand_set) == 3:
        for card in hand_set:
            if hand.count(card) == 3:
                hand_rank = 4
                break
            if hand.count(card) == 2:
                hand_rank = 3
                break
    # Check for one pair
    elif len(hand_set) == 4:
        hand_rank = 2
    # Check for high card
    else:
        hand_rank = 1
    return hand_rank


if __name__ == "__main__":
    HANDS = input_parse()
    for _hand in HANDS:
        _hand[2] = check_hand_rank(_hand[0])
    HANDS.sort(key=lambda x: (x[2], [ORDER.index(y)
               for y in x[0]]))
    print(HANDS)
    WINNINGS = 0
    for i, _hand in enumerate(HANDS):
        WINNINGS += int(_hand[1]) * (i + 1)
    print(WINNINGS)
