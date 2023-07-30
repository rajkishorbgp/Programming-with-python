'''
Write a program to remove duplicate characters from the given input string? input: 
ABCDABBCDABBBCCCDDEEEF output: ABCDEF
'''


def remove_duplicates(input_string):
    unique_chars = ""

    for char in input_string:
        if char not in unique_chars:
            unique_chars += char

    return unique_chars


# Test the program
user_input = input("Enter a string: ")
result = remove_duplicates(user_input)
print("Output:", result)

'''
Output:
Enter a string: ABCDABBCDABBBCCCDDEEEF
Output: ABCDEF
'''
