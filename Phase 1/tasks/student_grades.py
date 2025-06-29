# Your Mission:

# Create a script student_grades.py.
# Create a list of student names.
# Create a dict where keys are student names (from your list) and values are their corresponding grades (e.g., 88, 92, 75).
# Write code to calculate the average grade of all students.
# Pick one student. Use an f-string to print their name and grade.
# Create a set of all the subjects the students are taking (e.g., "Math", "Science"). Add a subject that's already there to prove that sets only store unique values.

names = ['Nishant', 'Ram', 'Suraj'] #This is a lists
grades = {      #dictionary
    'nishant': 88,
    'ram': 92,
    'suraj': 75
}

calulate_average_grade = sum(grades.values())/len(grades)

name = 'ram'
print(f'{name} scored: {grades[name]}')

subjects = {'DSA', 'OOP', 'Database'}
subjects.add('OOP')

print(f'The Subjects are: {subjects}')