"""In this we are going to perform some functions over the data presented in file
"""

filename = "StudentsPerformance.csv"

def operate_on_file(filename):
    """
    What is wrong here ?
        - for most common task we are ending up in writing a whole lot of code
          definitely there is a better way to do it    

    """
    with open(filename, 'r') as f:
        headers = next(f)     # skip the headers
        count = 0
        for line in f:
            count += 1
            print("Count: ", count)
            line = line.strip()
            line = line.split(',')
            line[5] = int(line[5].strip('"')) # remove extra "" and convert to int
            line[6] = int(line[6].strip('"')) # remove extra "" and convert to int
            line[7] = int(line[7].strip('"')) # remove extra "" and convert to int
            print (line)
            print('Total Score:', line[5] + line[6] + line[7])

operate_on_file(filename)
