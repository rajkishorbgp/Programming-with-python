'''
        Write a function to find factorial of given number?
'''


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Test the function
num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is: {result}")


'''
Output:
Enter a number: 6
The factorial of 6 is: 720

'''
