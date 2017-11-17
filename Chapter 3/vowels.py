vowels = ['a', 'e', 'i', 'o', 'u']
found = {}
for vowel in vowels:
    found[vowel] = 0

word = input("Provide a word to search for vowels: ")

for letter in word:
    if letter in vowels:
        found[letter] += 1

for vowel in found:
    print(vowel, 'was found', found[vowel], 'time(s).')