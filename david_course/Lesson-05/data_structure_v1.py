"""The portfolio example we did in the Lesson04 -v3. We are going
   to build a data structure by readking the file and will try to
   do more sophisticated computing using that data structure.
"""

import csv
filename = "StudentsPerformance.csv"

def read_student_marks(filename, *, errors='warn'):
    """
        Read the csv data into a list
    """
    school_details = []
    student_record = []
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("Errors must be one of 'warn', 'silent', 'raise'")
    with open(filename, 'r') as f:
        rows = csv.reader(f)     # wrap the csv module around the f
        headers = next(rows)     # skip the headers
        for rowno, row in enumerate(rows, start=1):
            try:                    
                row[5] = int(row[5]) # convert to int
                row[6] = int(row[6]) # convert to int
                row[7] = int(row[7]) # convert to int
            except ValueError as e:
                if errors == 'warn':
                    print ('Row no: ', rowno, 'Bad row: ', row)
                    print ('Row no: ', rowno, 'Reason: ', e)
                elif errors == 'raise':
                    raise                # Raise the last Exception
                else:
                    pass                 # Just Ignore the errors
                continue
            student_record = tuple(row)
            school_details.append(student_record)
    return school_details

school_records = read_student_marks(filename, errors='silent') # It makes it more readable


# Way 1
total_marks = 0
for record in school_records:
    total_marks = record[5] + record[6] + record[7]  # hard coding indices looks ugly
print("Total Marks for all Students in all subjects :", total_marks)

# Way 2
total_marks = 0
for gender, group, degree, standard, sth_else, math_score, reading_score, writing_score in school_records:
    total_marks = math_score + reading_score + writing_score # Though visually appealing but still what if tuple has many many records
print("Total Marks for all Students in all subjects :", total_marks)
