# Python 3.9
# Coding: utf-8
#########################################################################
# Calculating the Net Charge of Insulin by Using Python Lists and Loops #
#########################################################################
import os
path = os.path.abspath(os.getcwd()) + '//data'
# Function to read through a file, line by line, stores data to a variable:
def file2variable(filename):
    """" 
    This function opens and reads content in a file then them in a variable
    """
    with open(filename, 'r') as openFile:
        fileReader = openFile.readlines()
        variable = ''
        for row in fileReader:
            readLine = row.lower().strip(' ')
            variable += readLine
        openFile.close()
    return variable

# Exercise 1: Assigning variables, lists, and dictionaries
# Open and read file "preproInsulin-seq-clean.txt", store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = file2variable(path + '//preproInsulin-seq-clean.txt')
# Open and read files of remaining sequence elements of human insulin, store them in variables:
lsInsulin = file2variable(path + '//lsInsulin-seq-clean.txt')
bInsulin = file2variable(path + '//bInsulin-seq-clean.txt')
cInsulin = file2variable(path + '//cInsulin-seq-clean.txt')
aInsulin = file2variable(path + '//aInsulin-seq-clean.txt')
# Merge the results of the smaller insulin groupings into a single variable called insulin
insulin = str(bInsulin) + str(cInsulin)

# Create a code segment  dictionary:
pKR = {'y':10.07, 'c': 8.18, 'k':10.53, 'h':6.00, 'r':12.48, 'd':3.65, 'e':4.25}

# Exercise 2: Using count() to count the numbers of each amino acid
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
print(seqCount)

# Exercise 3: Writing the net charge formula
print('Calculating the net charge of insulin in pH values from 0 to 14:')
pH = 0
while pH <= 14:
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) for x in ['k','h','r']}.values())) 
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) for x in ['y','c','d','e']}.values()))
        )
    print('pH {0:.2f} : net charge of {1:.2f}'.format(pH, netCharge))
    pH += 1
