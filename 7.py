#

alphabet = list('abcdefghijklmnopqrstuvwxyz')
numbers = list(range(100))
print(alphabet)
print(numbers)

# 


a = [1, 2, 3]
b = list(a)

print(b)
a.append(4)
print(b)


# 

deck = []
for color in '♠', '♥', '♦', '♣': # (Use text names on Windows)
    for value in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
        deck.append(str(value) + color)
print(deck)

# -> two dimensional list 


# 

import random

deck = []
for color in '♠', '♥', '♦', '♣':
    for value in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
        deck.append(str(value) + color)
print(deck)

random.shuffle(deck)
print(deck)



# iterable = variable that can be iterated over, so 



