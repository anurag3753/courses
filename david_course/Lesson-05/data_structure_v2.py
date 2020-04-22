"""The portfolio example we did in the Lesson04 -v3. We are going
   to build a data structure by readking the file and will try to
   do more sophisticated computing using that data structure.

    - In this we will further improve by using davids choice for
      handling such scanerios

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
            # Make a dict instead of tuple, this way name access will be easy. David's choice
            student_record = {
                'gender' : row[0],
                'group'  : row[1],
                'degree' : row[2],
                'standard' : row[3],
                'sth_else' : row[4],
                'math_score' : row[5],
                'reading_score' : row[6],
                'writing_score' : row[7]
            }
            school_details.append(student_record)
    return school_details

school_records = read_student_marks(filename, errors='silent') # It makes it more readable
# print(school_records)

# Way 3
total_marks = 0
for  student_record in school_records:
    total_marks = student_record['math_score'] + student_record['reading_score'] + student_record['writing_score'] # David Choice
print("Total Marks for all Students in all subjects :", total_marks)
