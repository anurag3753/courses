"""Please finish the simple series first. That is forst to read
In this we are going to write a general level csv parsing module

- This is taken from Lesson5/v4 file

Why we need to do the type conversion manually. Better approach ?

"""
import csv

def read_csv(filename, types, *, errors='warn'):
    """ Read a csv with type conversion """

    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("Errors must be one of 'warn', 'silent', 'raise'")
    
    total = 0.0
    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)                # skip the header row
        for rowno, row in enumerate(rows, start=1):
            try:
                row = [ func(val) for func, val in zip(types, row) ]
            except ValueError as err:
                if errors == 'warn':
                    print ('Row no: ', rowno, 'Bad row: ', row)
                    print ('Row no: ', rowno, 'Reason: ', err)
                elif errors == 'raise':
                    raise                # Raise the last Exception
                else:
                    pass                 # Just Ignore the errors
                continue
            # Make a dict instead of tuple, this way name access will be easy. David's choice
            record = dict(zip(headers, row))
            records.append(record)
        return records