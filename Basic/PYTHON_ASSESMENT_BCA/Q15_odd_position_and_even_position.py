'''
                        Program: 15
    Write a program to print characters at odd position and even position 
    for the given String?
'''


def print_odd_even_characters(input_string):
    # Printing characters at odd positions
    print("Characters at odd positions:")
    for i in range(len(input_string)):
        if i % 2 == 0:
            print(input_string[i], end=" ")

    # Printing characters at even positions
    print("\nCharacters at even positions:")
    for i in range(len(input_string)):
        if i % 2 != 0:
            print(input_string[i], end=" ")


# Test the program
user_input = input("Enter a string: ")
print_odd_even_characters(user_input)


'''
Output:
Enter a string: rajkishorbgp
Characters at odd positions:
r j i h r g 
Characters at even positions:
a k s o b p 

'''
