"""In this new version, we have used the with statement, as with stmt
automatically takes care of closing the file once we are done with the file.

"""

filename = "StudentsPerformance.csv"

def read_file_at_once(filename):
    """This function reads the complete file in a single go and put it into a
    text string
    
    Arguments:
        filename {str} -- Name of the file
    """
    with open(filename, 'r') as f:
        data = f.read()
        print (data)

# Way 1
read_file_at_once(filename)

def read_file_line_by_line(filename):
    """This function reads the file line-by-line
    
    Arguments:
        filename {str} -- Name of file
    """
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='') # It removes the addition of extra newline while printing

# Way 2
read_file_line_by_line(filename)