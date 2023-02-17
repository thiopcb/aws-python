# Working with the String Sequence and Numeric Weight of Insulin in Python
##########################################################################
# Exercise 1: Assigning variables to the sequence elements of human insulin

# Define function to open and read content in a file then store them in a variable:
def file2variable(filename):
    openFile = open(filename, 'r')
    variable = ''
    readLine = openFile.readline().lower().strip(' ')
    variable += readLine
    while readLine != '':
        readLine = openFile.readline().lower().strip(' ')
        variable += readLine
    openFile.close()
    return variable

# Open and read file "preproInsulin-seq-clean.txt", store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = file2variable('preproInsulin-seq-clean.txt')
# Open and read files of remaining sequence elements of human insulin, store them in variables:
lsInsulin = file2variable('lsInsulin-seq-clean.txt')
bInsulin = file2variable('bInsulin-seq-clean.txt')
cInsulin = file2variable('cInsulin-seq-clean.txt')
aInsulin = file2variable('aInsulin-seq-clean.txt')
# Merge the results of the smaller insulin groupings into a single variable called insulin
insulin = str(bInsulin) + str(cInsulin)

# Exercise 2: Using print() to display sequences of human insulin to the console
# Printing "the sequence of human insulin" to console using successive print() commands:
print('The sequence of human preproinsulin: {}\nTotal of {} characters in this sequence\n'.format(preproInsulin, len(preproInsulin)))
print('The sequence of human insulin, chain ls: sequencing: {}'.format(lsInsulin))
print('The sequence of human insulin, chain b: sequencing: {}'.format(bInsulin))
print('The sequence of human insulin, chain c: sequencing: {}'.format(cInsulin))
print('The sequence of human insulin, chain a: sequencing: {}'.format(aInsulin))

# Exercise 3: Calculating the rough molecular weight of human insulin using the given code
# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19, 
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21, 
    'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12, 
    'V': 117.15, 'W': 204.23, 'Y': 181.19
}
# Count the number of each amino acids  
aaCountInsulin = ({x : float(insulin.upper().count(x)) for x in ['A', 'C', 
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 
'V', 'W', 'Y']})
# Multiply the count by the weights  
molecularWeightInsulin = round(sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values()), 2)
print('The rough molecular weight of insulin: {}'.format(molecularWeightInsulin))
# Calculate error percentage of rough molecular weight against actual molecular weight
molecularWeightInsulinActual = 5807.63
print("Error percentage: {}%".format(round(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100, 2)))
