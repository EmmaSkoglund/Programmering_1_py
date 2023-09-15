from collections import Counter

with open('numbers.txt', 'r') as file:
    numbers = file.read()

apperens = Counter(numbers)

print('-' * 15)
print('- NUMANALYZER -')
print('-' * 15)

for number in range(10):
    antal_forekomster = apperens[str(number)]
    print(f"| {number} | {antal_forekomster}")
print('-' * 15)
