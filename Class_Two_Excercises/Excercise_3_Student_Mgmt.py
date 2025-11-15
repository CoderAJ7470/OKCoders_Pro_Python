# Using a dictionary, create a student management system
  # Each student should have the following properties: name, age, grades list, courses list
  # Also write functions to
    # Add new students
    # Add student grades for existing students
    # Calculate each student's GPA
    # Find students by course name
    # Generate a report

import sys

# Dictionary that holds student data, with some initial student records
students = {
  'Nancy Dubois': {
    'Age': 18,
    'Courses': ['Math', 'English', 'Science', 'Geography'],
    'Grades': ['B', 'C', 'A', 'C']
  },
  
  'Bob Sainsbury': {
    'Age': 17,
    'Courses': ['Math', 'English', 'History', 'Biology'],
    'Grades': ['C', 'D', 'B', 'C']
  },

  'Travis Headley': {
    'Age': 20,
    'Courses': ['Math', 'English', 'History'],
    'Grades': ['C', 'D', 'B']
  }
}

# Adds new students to the dictionary
def add_student():
    student_name = input('Please enter the student name (first<space>last): ')
    student_age = int(input('Please enter the student age: '))

    course_one = input("Please enter the name of the student's course one: ")
    course_one_grade = input(f"Please enter the student's grade for {course_one}: ")

    course_two = input("Please enter the name of the student's course two: ")
    course_two_grade = input(f"Please enter the student's grade for {course_two}: ")

    course_three = input("Please enter the name of the student's course three: ")
    course_three_grade = input(f"Please enter the student's grade for {course_three}: ")

    course_four = input("Please enter the name of the student's course four: ")
    course_four_grade = input(f"Please enter the student's grade for {course_four}: ")

    courses_list = [course_one, course_two, course_three, course_four]
    grades_list = [course_one_grade, course_two_grade, course_three_grade, course_four_grade]

    new_student = {
      'Age': student_age,
      'Courses': courses_list,
      'Grades': grades_list
    }

    # Add the new student to the dictionary; the student's name will become the key for each nested dictionary a.k.a. the student's age, courses and grades for each course
    students[student_name] = new_student

# Add a course and associated grade for a given student
def add_course_and_grade():
    student_name = input('\nPlease enter the student name: ')
    course_name = input('Please enter the course name: ')
    course_grade = input(f'Please enter the student\'s current grade for {course_name}: ')

    if student_name not in students:
        print(f'\nYou entered the name "{student_name}"; this student is not in the records. If you want to add a new student, please choose Option 1 from the menu. Otherwise, please check the name and try again.')
    else:
        # Get the grades and courses list for this student, and add the new course/associated grade
        students[student_name]['Courses'].append(course_name)
        students[student_name]['Grades'].append(course_grade)

        print(f'Successfully added "{course_name}" and the grade of "{course_grade}" for {student_name} in the records.')

def get_student_GPA():
    match_found = False
    matched_name = ''

    # Get student name from user. Converting to lower case for comparison to name from dictionary - just a simple error-check on the input since Python is case-sensitive.
    student_name = input(
        '\nEnter the full name of the student whose GPA you would like to see, in the format <first> <last>: '
    ).lower()

    # As long as the user enters an incorrect name, keep asking. Once a matching name is found, proceed with calculating the GPA. Converting actual name to lower case here for comparison to user input.
    while not match_found:
        for full_name in students:
            if student_name in full_name.lower():
                matched_name = full_name
                match_found = True
                break

        if not match_found:
            print(f'\nHmm, I was not able to find a student by the name {student_name}.')
            student_name = input('Please check your spelling and try again: ')

    calculate_GPA(matched_name)

# Calculate the GPA for the student getting passed to this function
def calculate_GPA(name_of_student):
    accumulator = 0

    grade_points = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0
    }
    
    # Get the grades list for this student
    student_grades = students[name_of_student]['Grades']

    # Look at each grade in the list. Then look at the grade points for that grade from the grade_points dictionary (above), grab its value, add it to the accumulator. Repeat till all grades are covered.
    for grade in student_grades:
        if grade in grade_points:
            accumulator += grade_points[grade]

    GPA = accumulator / len(student_grades)

    print(f'\nThe GPA for {name_of_student} is {GPA:.1f}')

# Generate and print a stydent grade report
def show_student_report():
    # Returning a list of students from the dictionary
    student_list = list(students)

    print('\nShowing courses, grades and GPA for all students:')

    for student in student_list:
        print(f'\nName: {student}\n')

        courses = students[student]['Courses']
        grades = students[student]['Grades']

        print(f'Course and grade information for {student}:')
        for i in range(len(courses)):
            print(f'{courses[i]}: {grades[i]}')

        # Get student GPA
        GPA = calculate_GPA(student) 

        # Because we have a list from the students dictionary, we can check to see if we have reached the last index. We do not want this separator after the last student.
        if student != student_list[-1]:
            print('-------------------')

def show_students_by_course():
    students_taking_course = []
    course_name = input('Please enter the name of the course: ')
    names = ''

    for name, info in students.items():
        current_student_courses = info['Courses']

        if course_name in current_student_courses:
            students_taking_course.append(name)

    for student in students_taking_course:
        if student != students_taking_course[-1]:
            names += student + '; '
        else:
            names += student

    print(f'Students taking {course_name}: {names}')
    
# Shows the user a list from which they can choose, by entering the corresponding number
def show_choices():
    choice = ''

    print('Please choose an option from below (enter the number corresponding to what you would like to do and hit Enter):')

    while True:
        choice = input('\n"1" to add a new student | "2" to show a student report | "3" to add a course/grade for an existing student | "4" to show students by course name | "5" to calculate a student\'s GPA | "q" to exit: ')

        if choice == 'q':
            sys.exit(0)
        elif choice == '1':
            add_student()
        elif choice == '2':
            show_student_report()
        elif choice == '3':
            add_course_and_grade()
        elif choice == '4':
            show_students_by_course()
        elif choice == '5':
            get_student_GPA()
        else:
            print(f'\nSorry, {choice} is not a valid choice. Please enter a number corresponding to one of the choices below, and hit Enter:\n')
        
# Runs the whole program
def run_program():
    show_choices()

run_program()