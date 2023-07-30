''' 
Reverse Vowels in a String USING function
'''


def is_vowel(char):
    vowels = "AEIOUaeiou"
    return char in vowels


def reverse_vowels(input_string):
    vowels = [char for char in input_string if is_vowel(char)]
    reversed_vowels = vowels[::-1]

    result = ""
    vowel_index = 0

    for char in input_string:
        if is_vowel(char):
            result += reversed_vowels[vowel_index]
            vowel_index += 1
        else:
            result += char

    return result


# Test the function
user_input = input("Enter a string: ")
result = reverse_vowels(user_input)
print("String with reversed vowels:", result)

'''
output:
Enter a string: aeiouaeiou
String with reversed vowels: uoieauoiea
'''
