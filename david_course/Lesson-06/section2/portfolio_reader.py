"""This file is in sequence to general_purpose_csv_library.
    We are using our library module now to read the portfolio
"""
import general_pupose_csv_library

def read_portfolio(filename, *, errors='warn'):    
    return general_pupose_csv_library.read_csv(filename, [str, str, int, float], errors=errors)

if __name__ == "__main__":
    portfolio = read_portfolio('stocks_dummy.csv')
    total = 0.0
    for holding in portfolio:
        total += holding['shares'] * holding['price']

    print("Total cost:", total)