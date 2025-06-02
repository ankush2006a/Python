''' Assignment 5 Task 1 '''

student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92,
    "Eve": 88
}
student_name = input("Enter the student's name: ")
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")

'''Assignment 5 Task 2 '''

numbers = list(range(1, 11))
first_five = numbers[:5]
reversed_five = first_five[::-1] 
print(f"Original list: {numbers}")
print(f"Extracted first five elements: {first_five}")
print(f"Reversed extracted elements: {reversed_five}")
