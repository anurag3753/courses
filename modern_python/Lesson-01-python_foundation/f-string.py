"""We are going to learn about f-sting. It is the default formatting
choice after python3.6.
Technical Details :- The format {x} gets compiled whenever we run python <myfile.py>.
Since this happen at compile time, it is more efficient and there is no security
flow also.
"""

"""Use 1: Simple Way
"""

x = 10
print(f'The answer is {x} today')

"""Use 2: Using the formatting operators.
They have look and feel of key-value pairs.
"""
print(f'The anuswer is {x : 8} today')       # it will make it 8 characters wide
print(f'The anuswer is {x : 08} today')      # it will make it 8 characters wide with leading zeros

"""Use 3 :- Running small epression
"""
print(f"the squre of x is {x ** 2 : 8d}")    # Small expression written inside the formatted string. d retruns it as decimal value

"""Use 4 :- Raising Exception Mesages
Pronounced as :- x bang r. Expected the representation to be a float 
"""
raise ValueError(f'Expected {x!r} to a float not a {type(x).__name__}')  # Used in frameworks