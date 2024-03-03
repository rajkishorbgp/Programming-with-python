''''
                        Program:17
    Write a program for the following requirement input: a4b3c2 output: aaaabbbcc.
    
'''


def expand_string(input_string):
    expanded_string = ""
    i = 0

    while i < len(input_string):
        char = input_string[i]
        count = int(input_string[i+1])
        expanded_string += char * count
        i += 2

    return expanded_string


# Test the program
user_input = input("Enter a string: ")
expanded_result = expand_string(user_input)
print("Output:", expanded_result)


'''
Output:
Enter a string: a4b3c2
Output: aaaabbbcc

'''
