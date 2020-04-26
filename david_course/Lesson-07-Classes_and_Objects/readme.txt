Classes :-
    The name of the class, serves as a function, that is used to create instances. The purpose of init is to save
    the data.

    Core Operations allowed on python Classes:- (only 3 Operations)
        - set               # holding.name = "tcs"             = setattr(holding, 'name', 'tcs')
        - get               # print(holding.name)              = getattr(holding , 'name')
        - delete            # del holding.name                 = delattr(holding, 'name')

    There is nothing as private and protected in python. So, your variables are exposed to everyone.
    
    - Drawback 1:
        holding.name = "tcs"
        holding.nme  = "ibm"        # Typo error, resulted in 2 different attributes in python class, we surely don't want that

    There is another way to get the attributes, out of the system, we can use the (get, set, del) attr machinery. And knowing
    about this, gives additional power to the user.
    You can use setattr, getattr, delattr to write extremely general code.

    Alternate onstructors:-
        Since a class can only have one init function, if you want to have more than one initializers, then how to do that ??
            - We uses @classmethod . See dateobj.py for details
            - variables defined inside the init are specfic to the instances
            - variables defined inside the class are shared by all the class instances. Ex `class version`. A good choice is to
              use string for version.
    
    Use of static method:-
        