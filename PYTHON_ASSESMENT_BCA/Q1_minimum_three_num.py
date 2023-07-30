'''
            Program 1
    Program for minimum of 3 numbers.
'''

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third  number: "))

if a < b and a < c:
    print(a, " is minimum of 3 numbers")
elif b < c and b < a:
    print(b, "is minimum of 3 numbers")
else:
    print(c, "is minimum of 3 numbers")

'''
Output:
Enter the first number: 10
Enter the second number: 30
Enter the third  number: 20
10  is minimum of 3 numbers

'''
