"""In this we are going to see the use of try/except block
    Along with that, we can remove rowno incrementation when we are using
    a for loop
"""

import csv
filename = "StudentsPerformance.csv"

def operate_on_file(filename):
    """
        - Focus is on using enumerate to avoid use of the rowno variable
        - This code still suffers from problem of creating `print` stmts as
          sideeffect of your function, to which user has no control
        - In next verion we will resolve this issue.

    """
    with open(filename, 'r') as f:
        rows = csv.reader(f)     # wrap the csv module around the f
        headers = next(rows)     # skip the headers
        for rowno, row in enumerate(rows, start=1):
            try:                    
                row[5] = int(row[5]) # convert to int
                row[6] = int(row[6]) # convert to int
                row[7] = int(row[7]) # convert to int
            except ValueError as e:
                print ('Row no: ', rowno, 'Bad row: ', row)
                print ('Row no: ', rowno, 'Reason: ', e)
                continue
    print('Total Marks for all Students in all subjects:', row[5] + row[6] + row[7])

operate_on_file(filename)
