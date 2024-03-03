'''
                        program: 4
    Write a program to read Employee data from the keyboard and print that data.

'''


def readEmployeedata():
    name = input("Enter the Employee name: ")
    employee_no = int(input("Enter the Employee number: "))
    employee_salary = float(input("Enter the Employee salary: "))
    employ_deta = {"name": name, "employee_no": employee_no,
                   "employee_salary": employee_salary}
    return employ_deta


employ_deta = readEmployeedata()
# print Employee data
print("\n________Employee data______")
print("Employee name: ", employ_deta["name"])
print("Employee number", employ_deta["employee_no"])
print("Employee salary", employ_deta["employee_salary"])


'''
Output:
Enter the Employee name: Raj kishor
Enter the Employee number: 6095
Enter the Employee salary: 1500000

________Employee data______
Employee name:  Raj kishor
Employee number 6095
Employee salary 1500000.0

'''
