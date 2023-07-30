'''
                        Program: 13
    Program to display all positions of substring in a given main string
'''


def find_all_positions(main_string, sub_string):
    positions = []
    index = 0

    while index < len(main_string):
        index = main_string.find(sub_string, index)
        if index == -1:
            break
        positions.append(index)
        index += 1

    return positions


main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to search: ")

positions = find_all_positions(main_string, sub_string)

if positions:
    print(f"Substring '{sub_string}' found at positions: {positions}")
else:
    print("Substring not found in the main string.")
