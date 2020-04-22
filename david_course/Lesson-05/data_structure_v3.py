"""In v2 we did a data structure creation. Now we will see that after we
are done with data sctucture, the most common thing that we do is - 
    iterate over the data structure using a for loop and :-
        - do operations like filtering, appending, summing up the data
    - Since these tasks are so common, python has a useful feature of list
      comprehension to handle such things

"""

import csv
from data_structure_v2 import read_student_marks
filename = "StudentsPerformance.csv"

school_records = read_student_marks(filename, errors='silent') # It makes it more readable

# Common Paradigms

## 1st - Loop Over and summing up [Collect total marks]
total_marks = 0
for  student_record in school_records:
    total_marks = student_record['math_score'] + student_record['reading_score'] + student_record['writing_score'] # David Choice
print("Total Marks for all Students in all subjects :", total_marks)

## 2nd - Loop Over and Collect Items [Collect all the math_scores]
all_math_scores = []
for  student_record in school_records:
    all_math_scores.append(student_record['math_score'])
print("All Math scores:", all_math_scores)

## 3rd - Loop over and apply filters [ Collect all the math scores above 70]
all_math_scores = []
for  student_record in school_records:
    if student_record['math_score'] > 70:
        all_math_scores.append(student_record['math_score'])
print("Above 70 Math scores:", all_math_scores)

# To Handle such scanerios a powerful approach is to use list comprehension


## Solution to 1st
total_marks = sum(student_record['math_score'] + student_record['reading_score'] + student_record['writing_score'] for student_record in school_records)
print("Total Marks for all Students in all subjects :", total_marks)

# Solution to 2nd
all_math_scores = [student_record['math_score'] for student_record in school_records]
print("All Math scores:", all_math_scores)

## Solution to 3rd
above_70_score_students = [student_record['math_score'] for student_record in school_records if student_record['math_score'] > 70 ]
print("Above 70 Math scores:", above_70_score_students)

# 72 appears twice. Now goal is to get unique scores in the provided all maths scores --> Refer Solution to 2nd
all_math_scores_unique = {student_record['math_score'] for student_record in school_records}       # Change to set
print("All Math scores unique:", all_math_scores_unique)