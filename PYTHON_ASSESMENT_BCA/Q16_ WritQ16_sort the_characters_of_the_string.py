'''
                                Program: 16
    Write a program to sort the characters of the string and first alphabet symbol 
    followed by numeric values input: B4A1D3 Output: ABD134
'''


def sort_alphanumeric(input_string):
    alphabets = []
    numerics = []

    for char in input_string:
        if char.isalpha():
            alphabets.append(char)
        elif char.isnumeric():
            numerics.append(char)

    sorted_string = ''.join(sorted(alphabets) + sorted(numerics))
    return sorted_string


# Test the program
user_input = input("Enter a string: ")
sorted_result = sort_alphanumeric(user_input)
print("Output:", sorted_result)


'''
Output:
Enter a string: B4A1D3
Output: ABD134

'''
