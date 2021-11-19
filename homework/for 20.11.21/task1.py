file = open("karenina.txt", "r", encoding="utf-8")
text = file.read().upper()

all_letters = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
letter_dict = {}
for letter in all_letters:
    letter_dict[letter] = text.count(letter) # Так же можно? Да?..

items = list(letter_dict.items())
items.sort(key=lambda item: item[1])
items.reverse()

print("TOP 5 LETTERS:")
for place in range(1, 6):
    print(f"Place {place}: {items[place][0]} - {items[place][1]} times")