'''
                            Program: 20
    Write a program to display unique vowels present in the given word?
    
'''


def find_unique_vowels(input_word):
    vowels = "AEIOUaeiou"
    unique_vowels = set()

    for char in input_word:
        if char in vowels:
            unique_vowels.add(char)
    return unique_vowels


# Test the program
user_input = input("Enter a word: ")
result = find_unique_vowels(user_input)

print("Unique vowels in the word:", result)

'''
Output:
Enter a word: rajkishor
Unique vowels in the word: {'a', 'o', 'i'}

'''
