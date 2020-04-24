I wrote readme for this section explicitly, because it deals with how to create a package.
    - When you work with larger collections of code, one challange that comes up, is how to 
       organize your code modules. The standard way of handling this is to create a package.
    
    Lets do this exercise for the portfolio reader created in section2

    - The way you do that :- < Root dir for experiment is portie dir >
        - first create a dir [portie], which will act as the container for your code.
        - mkdir portfolio_reader
        - then I copied general_purpose_csv_library.py and portfolio_reader.py into it from sectio2
        - Add __init__.py file too

    Try this :- It works
        - import portie.general_pupose_csv_library
        - print(portie.general_pupose_csv_library.read_csv('stocks_dummy.csv', [str, str, int, float]) ) ## it works
    
    Try this :- It fails
        - import portfolio_reader.portfolio_reader
            >> it fails ModuleNotFoundError: No module named 'general_pupose_csv_library'
        
        Reason :- Is `general_pupose_csv_library` is part of my code OR is it someone else package ??
                  python does not really know these things
            
        Fix :-

        Way1:-  # Assumes a top-level import
            
            - Change the `import general_pupose_csv_library` 
                        --> `import portie.general_pupose_csv_library` in portfolio_reader.py
              and you also need to change the places where you are referring to the general_pupose_csv_library() 
                        --> `portie.general_pupose_csv_library`
        
        Way2:- # Assumes a package relative import

            - Change the `import general_pupose_csv_library` 
                        ---> from . import general_pupose_csv_library in portfolio_reader_v2.py
              and you don't have to make changes as we did in case 1

            - One more advantage is, if you decide to change the name of your package, you can just rename it to sth else
              without touching the code at all.

Use of __init__.py

    - It will execute, When the code is loaded. i.e when the import is done
        `import portie.portfolio_reader_v2` :- will run this file
        `import portie.general_pupose_csv_library` :- will also run this file

    - One use of this file, is to do the intialization steps for the package.
    - Another use, is to load the symbols from the submodules, into one collective space, to make it one level up
    - Check the init.py, I have lift up the symbols from the lower level to top level. This simplifies user life.
        - Now you can do
            - `import portie`
            - `portie.read_portfolio()`

    In short, its use case is to glue up a package together, so that user does not have to worry about a lot.

    Caution :- If there are Cross-references between modules, then you need to fix the import statements