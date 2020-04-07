"""The idea is here to see, how should we design our function
"""

import csv
filename = "StudentsPerformance.csv"

def operate_on_file(filename, *, errors='warn'):
    """
        - Get more control over your function
        - Using * force people to use keyword on args [keyword passing style]
    """
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
    print('Total Score:', row[5] + row[6] + row[7])

operate_on_file(filename, errors='silent') # It makes it more readable