"""Understanding the classes:- 
    Consider it reading after holding_v2.py
    We are going to see class methods and alternate constructors in this section
"""

class Date:
    ''' An advanced Date class
    '''

    version = '1.2'                   # This will be shared by all the instances of the class

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod                        # Alternate constructor
    def from_string(cls, s):
        parts = s.split('-')
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))


def main():
    # Ways of creating objects from classes

    ## Way 1
    date_default = Date(2007,8,11)
    print(date_default.year)

    ## Way2
    date_from_string = Date.from_string('2007-08-11')
    print(date_from_string.year)
    

if __name__ == '__main__':
    main()