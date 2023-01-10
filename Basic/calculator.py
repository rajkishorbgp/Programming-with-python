num1= int(input("Enter first number: "))
op= input("Enter operator(+, -, *, /): ")
num2= int(input("Enter second number: "))

"""
type casting

int()
float()
str()
bool()

"""

if op=='+':
    print(int(num1)+int(num2))
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1/num2)
else:
    print("invalid Operatior...")


# Output
"""
Enter first number: 7
Enter operator(+, -, *, /): /
Enter second number: 3
2.3333333333333335
"""