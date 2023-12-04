"""Day 4 part 2"""


cards = []

with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split(':')[1].strip()
        winning = line.split('|')[0].strip().split(" ")
        my = line.split('|')[1].strip().split(" ")
        cards.append({
            'winning': winning,
            'my': my,
            'total': 1,
        })

TOTAL_SCARTCHCARDS = 0
for i, card in enumerate(cards):
    wins = 0
    for win in card['winning']:
        if win == '':
            continue
        wins += card['my'].count(win)
    matchings = wins
    for j in range(i + 1, i + 1 + int(matchings)):
        cards[j]['total'] += 1 * card['total']


for card in cards:
    TOTAL_SCARTCHCARDS += card['total']

print(TOTAL_SCARTCHCARDS)
