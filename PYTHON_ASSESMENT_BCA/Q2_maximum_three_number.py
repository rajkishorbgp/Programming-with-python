'''
            Program 2
    Program for maximum of 3 numbers.
'''

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third  number: "))

if a > b and a > c:
    print(a, " is minimum of 3 numbers")
elif b > c and b > a:
    print(b, "is minimum of 3 numbers")
else:
    print(c, "is minimum of 3 numbers")

'''
Output:
Enter the first number: 20
Enter the second number: 10
Enter the third  number: 30
30 is minimum of 3 numbers

'''
