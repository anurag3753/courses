"""Understanding the classes:- 
    We are not using Holding(object) syntax, because in python3 all the classes by default 
    inherit from object classes
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

def main():
    h = Holding('tcs', '25apr', 100, 1500)
    print(h.shares)                         # It access the value stored in shares for instance `h`
    print(h.cost())                         # It does the calculation on shares and price
    """
    h.cost() == (h.cost)()

    It turns out that h.cost() is two completely seperate things going on :-
        - (h.cost)  # 1st part is the lookup of the attribute
        - if lookup is successfull, then there is a function call done for that i.e. (h.cost) ()

    You can also do one without the other, like
    >>> c = h.cost              # it returns a method attached to the holding object
    >>> c()


    """

    # Using list comprehension on the objects to compute the total portfolio valuation
    holding = read_portfolio("stocks_dummy.csv")            # Read the portfolio into a list of objects
    valuation = sum([h.shares* h.price for h in holding])
    print(valuation)

    ## Everything works as it is, as we were doing it before, but now we are creating instances and using the .(dot)
    ## operator to do the same computation


if __name__ == "__main__":
    main()