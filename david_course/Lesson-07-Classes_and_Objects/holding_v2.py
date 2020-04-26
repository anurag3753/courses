""" Using the get, set machinery
"""

class Holding:
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

"""
Lets see a stripped down version of read_portfolio written usign the classes
"""
import csv
def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            h = Holding(row[0], row[1], int(row[2]), float(row[3]))
            portfolio.append(h)
    return portfolio

def print_table(objects, colnames):
    """
    Make a nicely formatted table showing the attributes from a list of objects
    """
    for colname in colnames:
        print(f"{colname:>10}", end = ' ')
    print()
    for obj in objects:
        for colname in colnames:
            print(f"{getattr(obj, colname):>10}", end = ' ')
        print()

def main():
    h = Holding('tcs', '25apr', 100, 1500)
    setattr(h, 'date', '28apr')             # It sets the attribute using the setattr. Updated date to 28 apr
    print(getattr(h, 'date'))               # Get the value using the getattr
    print(getattr(h, 'shares'))             # It access the value stored in shares for instance `h` using getattr
    print(h.cost())                         # It does the calculation on shares and price using getattr
    """
    h.cost() == (h.cost)()

    It turns out that h.cost() is two completely seperate things going on :-
        - (h.cost)  # 1st part is the lookup of the attribute
        - if lookup is successfull, then there is a function call done for that i.e. (h.cost) ()

    You can also do one without the other, like
    >>> c = h.cost              # it returns a method attached to the holding object
    >>> c()


    """

    """ We can use the get set machinery, to write extremely general code. Ex"""
    output_columns = ['name', 'shares', 'price']            ## You have control on what to see in output
    for column_name in output_columns:
        print(column_name, "=", getattr(h, column_name))

    # Read portfolio in a nicely formatted table
    portfolio = read_portfolio("stocks_dummy.csv")
    print_table(portfolio, ['name', 'shares'])              ## You can pick what you want

if __name__ == "__main__":
    main()