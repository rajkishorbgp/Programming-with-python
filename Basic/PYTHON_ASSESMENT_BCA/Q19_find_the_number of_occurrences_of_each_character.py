'''
                        Program: 19
    Write a program to find the number of occurrences of each character present 
    in the given String? input: ABCABCABBCDE output: A-3,B-4,C-3,D-1,E-1
'''


def count_occurrences(input_string):
    occurrences = {}

    for char in input_string:
        occurrences[char] = occurrences.get(char, 0) + 1

    return occurrences


# Test the program
user_input = input("Enter a string: ")
result = count_occurrences(user_input)

print("Output:", end=" ")
for char, count in result.items():
    print(f"{char}-{count}", end=", ")


'''
Output:
Enter a string: ABCABCABBCDE
Output: A-3, B-4, C-3, D-1, E-1,

'''
