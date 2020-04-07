"""I have downloaded some dummy data from Kaggle and only kept 10 entries and 
removed rest of the entries.

Idea: Lets understand how to do some of the file processing in python

"""

filename = "StudentsPerformance.csv"

def read_file_at_once(filename):
    """This function reads the complete file in a single go and put it into a
    text string
    
    Arguments:
        filename {str} -- Name of the file
    """
    f = open(filename, 'r')
    data = f.read()
    print (data)
    f.close()

# Way 1
read_file_at_once(filename)

def read_file_line_by_line(filename):
    """This function reads the file line-by-line
    
    Arguments:
        filename {str} -- Name of file
    """
    f = open(filename, 'r')
    for line in f:
        print(line, end='') # It removes the addition of extra newline while printing
    f.close()

# Way 2
read_file_line_by_line(filename)
