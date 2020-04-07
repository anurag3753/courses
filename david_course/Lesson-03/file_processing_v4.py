"""In this we are going to explore csv module in python
"""

import csv
filename = "StudentsPerformance.csv"

def operate_on_file(filename):
    """
        - Compare it with the version 3
        - With the standard module, we no longer need to remove the extra " as
          it is auto getting take care in csv module
        - However we still need to typecast to int 

    """
    with open(filename, 'r') as f:
        rows = csv.reader(f)     # wrap the csv module around the f
        headers = next(rows)     # skip the headers
        count = 0
        for row in rows:
            count += 1
            print("Count: ", count)
            row[5] = int(row[5]) # convert to int
            row[6] = int(row[6]) # convert to int
            row[7] = int(row[7]) # convert to int
            print (row)
            print('Total Score:', row[5] + row[6] + row[7])

operate_on_file(filename)
