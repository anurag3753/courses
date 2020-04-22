"""In this we are writing a function to read the portfolio
    which will be used in v5
"""
import csv

def read_portfolio(filename, *, errors='warn'):
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("Errors must be one of 'warn', 'silent', 'raise'")
    
    total = 0.0
    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)                # skip the header row
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print ('Row no: ', rowno, 'Bad row: ', row)
                    print ('Row no: ', rowno, 'Reason: ', e)
                elif errors == 'raise':
                    raise                # Raise the last Exception
                else:
                    pass                 # Just Ignore the errors
                continue
            # Make a dict instead of tuple, this way name access will be easy. David's choice
            record = {
                'name' : row[0],
                'date'  : row[1],
                'shares' : row[2],
                'price' : row[3],
            }
            portfolio.append(record)
        return portfolio

# portfolio = read_portfolio('stocks_dummy.csv')

# total = 0.0
# for holding in portfolio:
#     total += holding['shares'] * holding['price']

# print("Total cost:", total)