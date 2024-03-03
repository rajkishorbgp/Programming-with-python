'''
                                Program: 21
    Write a program to enter name and percentage marks in a dictionary and display 
    information on the screen.
    
'''


def get_student_info():
    student_info = {}
    while True:
        name = input("Enter student name (or type 'exit' to stop): ")
        if name.lower() == 'exit':
            break
        percentage = float(input("Enter percentage marks: "))
        student_info[name] = percentage
    return student_info


def display_student_info(student_info):
    print("\nStudent Information:")
    for name, percentage in student_info.items():
        print(f"Name: {name}, Percentage Marks: {percentage}%")


# Main program
if __name__ == "__main__":
    print("Enter student names and percentage marks. Type 'exit' to stop.")

    student_data = get_student_info()
    display_student_info(student_data)

'''
Output
Enter student names and percentage marks. Type 'exit' to stop.
Enter student name (or type 'exit' to stop): Raj kishor
Enter percentage marks: 85
Enter student name (or type 'exit' to stop): muskan
Enter percentage marks: 83
Enter student name (or type 'exit' to stop): ram
Enter percentage marks: 87
Enter student name (or type 'exit' to stop): exit

Student Information:
Name: Raj kishor, Percentage Marks: 85.0%
Name: muskan, Percentage Marks: 83.0%
Name: ram, Percentage Marks: 87.0%

'''
