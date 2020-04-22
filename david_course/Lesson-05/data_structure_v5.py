"""We are going to implement tail(linux) functionality in python
    - For this we are going to create a dummy data for the stocks
    that we are holding and we will try to get the live data using
    yahoo finanace and then we will try to see, if we are doing good
    w.r.t the stock market or not
"""

from data_structure_v4 import read_portfolio

portfolio = read_portfolio('stocks_dummy.csv')

total = 0.0
for holding in portfolio:
    total += holding['shares'] * holding['price']

print("Total cost:", total)

# unique_stock_names
unique_names = { holding['name'] for holding in portfolio}
print(unique_names)

# creating a string from a set/list
unique_names_string = ','.join(unique_names)
print(unique_names_string)

"""
We are not able to open this url as of now, but its output is a list of pries rquested for the required stocks
Here the requested stocks are -- unique_names_string

>>> import urllib.request
>>> u = urllib.request.urlopen('http://finance.yahoo.com/d/quotes.csv?s={}&f=l1'.format(unique_names_string))
>>> data = u.read()
>>> pricedata = data.split()

We are directly going to assume a list of price values returned
>>> returned_prices = ['72.51', '9.27', '153.74', '30.23', '53.00']

"""
returned_prices = ['72.51', '9.27', '153.74', '30.23', '53.00']

## Lets pair these new prices with the shares names 	                                    # zip usage
for name, price in zip(unique_names, returned_prices):
    print(name, '=', price)

## Smarter way
prices = dict(zip(unique_names, returned_prices))
print(prices)

## Price data is not converted properly, so we can not directly do calculations on it.
## Hence we are going to convert the data properly, so that we can do calculations on it
prices = {name : float(price) for name, price in zip(unique_names, returned_prices)}        # dict comprehension
print(prices)

## Let's do one more thing
"""
We are getting abnormal behavior below, because we have the data distributed in our portfolio
We need to have one column per stock, but we have many based on their date of purchase
So, we need to aggregate the portfolio. 
I have left it as it is, but it will not do the job properly
"""
current_portfolio = sum(holding['shares']* prices[holding['name']] for holding in portfolio)
print('current_portfolio :', current_portfolio)

## Am I in profit ??
change = current_portfolio - total
print('change in portfolio :', change)
