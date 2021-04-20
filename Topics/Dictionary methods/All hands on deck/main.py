cards = [str(x) for x in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
card_values = dict(zip(cards, list(range(2, 15))))

items = 6
total_value = 0

for _ in range(items):
    total_value += card_values[input()]

print(total_value / items)
