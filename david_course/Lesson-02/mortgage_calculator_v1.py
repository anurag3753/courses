"""
    This is a simple program to tell you amount the user has finally paid to
    come out of all his debts.
    Observation :-
        paying almost double the amount to get rid of this simple loan. We will
        enhance it to v2, to play a scanerio
"""
principal = 500000
payment = 2684.11
rate = 0.05
total_paid = 0

while principal > 0:
    interest = principal * ( rate / 12 )
    principal = principal + interest - payment
    total_paid += payment

print('Total paid:', total_paid)
