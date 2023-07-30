'''
Write a program to accept student name and marks from the keyboard and creates a 
dictionary. Also display student marks by taking student name as input?
'''


def create_student_dict():
    student_dict = {}
    while True:
        name = input("Enter student name (or type 'exit' to stop): ")
        if name.lower() == 'exit':
            break
        marks = float(input("Enter student marks: "))
        student_dict[name] = marks
    return student_dict


def display_student_marks(student_dict, name):
    if name in student_dict:
        marks = student_dict[name]
        print(f"{name}'s marks: {marks}")
    else:
        print(f"{name} not found in the student records.")


# Main program
if __name__ == "__main__":
    print("Enter student names and marks. Type 'exit' to stop.")

    student_data = create_student_dict()

    while True:
        student_name = input(
            "Enter student name to get their marks (or type 'exit' to stop): ")
        if student_name.lower() == 'exit':
            break
        display_student_marks(student_data, student_name)

'''
Output:
Enter student names and marks. Type 'exit' to stop.
Enter student name (or type 'exit' to stop): Raj kishor
Enter student marks: 85
Enter student name (or type 'exit' to stop): ram
Enter student marks: 80
Enter student name (or type 'exit' to stop): muskan
Enter student marks: 88
Enter student name (or type 'exit' to stop): exit
Enter student name to get their marks (or type 'exit' to stop): exit
'''
