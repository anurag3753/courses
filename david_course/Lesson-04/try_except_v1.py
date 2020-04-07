"""In this we are going to see the use of try/except block
"""

import csv
filename = "StudentsPerformance.csv"

def operate_on_file(filename):
    """
        - Files could have missing values for some columns
        - Use try/except block to handle such scanerios
        - We should always use the specific errors
        - Never use `except Exception as e`
        

    """
    with open(filename, 'r') as f:
        rows = csv.reader(f)     # wrap the csv module around the f
        headers = next(rows)     # skip the headers
        rowno = 0
        for row in rows:
            rowno += 1
            try:                    
                row[5] = int(row[5]) # convert to int
                row[6] = int(row[6]) # convert to int
                row[7] = int(row[7]) # convert to int
            except ValueError as e:
                print ('Row no: ', rowno, 'Bad row: ', row)
                print ('Row no: ', rowno, 'Reason: ', e)
                continue
    print('Total Score:', row[5] + row[6] + row[7])

operate_on_file(filename)
