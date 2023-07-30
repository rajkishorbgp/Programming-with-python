'''
                            Program: 7
    To display the sum of first n numbers using while or for loop.
'''

num = int(input("Enter the number you want to sum up to first number: "))

sum = 0
count = num
print("\n_____Using while loop_____")
while (count):
    sum += count
    count -= 1
print("sum up to first number: ", sum)

sum = 0
print("\n_____Using for loop_____")
for i in range(num+1):
    sum += i
print("sum up to first number: ", sum)

'''
Output:
Enter the number you want to sum up to first number: 10

_____Using while loop_____
sum up to first number:  55

_____Using for loop_____
sum up to first number:  55

'''
