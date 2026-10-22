#create a list of even numbers from 0 to 20 using below list
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_numbers = [x for x in list if x % 2 == 0]
print(even_numbers)

# create a list of numbers upto 100 which are divisible by 10
divisible_list = []
for i in range(101):
    if i % 10 == 0:
        divisible_list.append(i)
print(divisible_list)  # Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Write a program to display unique vowels present in the given word
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Enter a word: ")
found_vowels = []
for char in word:
    if char in vowels and char not in found_vowels:
        found_vowels.append(char)
print("Unique vowels in the word:", found_vowels)

