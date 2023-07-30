'''
                        Program: 8
    write a program to prompt user to enter some name and password 
    until entering MIT and 123@321.

'''

name = "MIT"
password = "123@321"

while True:
    use_name = input("Enter the name: ")
    if name == use_name:
        use_password = input("Enter the password: ")
        if password == use_password:
            break
        else:
            print("invalid password!!")
    else:
        print("invalid name")
print("Welcome to mit college!!!")

'''
Output:
Enter the name: raj
invalid name
Enter the name: MIT
Enter the password: 123@123
invalid password!!
Enter the name: MIT
Enter the password: 123@123
invalid password!!
Enter the name: MIT
Enter the password: 123@321
Welcome to mit college!!!

'''
