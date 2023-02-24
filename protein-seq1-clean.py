# Python 3.9
# Coding: utf-8
############################################
# Preparing to Analyze Insulin with Python #
############################################

# Exercise 1: Retrieving the protein sequence of human preproInsulin
# The National Center for Biotechnology Information (NCBI) has information on many biological sequences.
# 1. Access NCBI at https://ncbi.nlm.nih.gov.
# 2. Next to the search bar, choose the dropdown menu and select Protein. Next, in the search bar, enter human insulin and choose Search.
# 3. Choose the following search result: insulin [Homo sapiens].
# 4. At the bottom of the search record, copy the insulin sequence, which starts with the word ORIGIN and ends with //.
# 5. Paste the insulin sequence into a file "preproInsulin-seq.txt".
# Bonus: Cleaning preproInsulin-seq.txt programmatically

# Exercise 2: Obtaining the protein sequence of human insulin
import os
path = os.path.abspath(os.getcwd()) + '//data'

def lineProcessing(line):
    """ This function omits out characters in a line text: '1', '6' and whitespaces """
    text = ''
    for char in line:
        if char == '1' or char == '6' or char == ' ':
            text = text + ''
        else:
            text += char
    return text

# Read first line from file
# readfileLine = filepreproInsulin.readline().lower().strip(' ')

# filepreproInsulin = open(path + '//preproinsulin-seq.txt', 'r') # open and read file to variable
tempText = '' # initialize temperory line text variable
preproInsulin ='' # Store the human preproInsulin sequence in a variable called preproInsulin
# Loop through a file to copy line by line until end of line:
with open(path + '//preproinsulin-seq.txt', 'r') as textFile:
    fileReader = textFile.readlines()
    for row in fileReader:
        # Check line to ignore key text: 'origin' and '//'
        if 'origin' not in row.lower():
            tempText = lineProcessing(row).strip(' ').strip('\n')
            if '//' in row:
                preproInsulin += ''
            else:
                preproInsulin += tempText
        else:
            None
textFile.close() # close working file after cleaning sequence

# Write cleaned sequence to text file, preproInsulin-seq-clean.txt
with open(path + '//preproInsulin-seq-clean.txt', 'w') as textFile:
    textFile.write(preproInsulin)
textFile.close() # close working file after cleaning sequence

# Store the remaining sequence elements of human insulin in variables
lsInsulin = ''
bInsulin = ''
cInsulin = ''
aInsulin = ''

# Loop through first sequence, lsInsulin, 24 characters
for charlsInsulin in preproInsulin[0:24]:
    lsInsulin += charlsInsulin
# Loop through second sequence, bInsulin, 30 characters
for charbInsulin in preproInsulin[24:54]:
    bInsulin += charbInsulin
# Loop through third sequence, cInsulin, 35 characters
for charcInsulin in preproInsulin[54:89]:
    cInsulin += charcInsulin
# Loop through fourth sequence, aInsulin, 21 characters
for charaInsulin in preproInsulin[89:110]:
    aInsulin += charaInsulin

# Write cleaned sequences to text file
with open(path + '//lsInsulin-seq-clean.txt', 'w') as textFile:
    textFile.write(lsInsulin)
with open(path + '//bInsulin-seq-clean.txt', 'w') as textFile:
    textFile.write(bInsulin)
with open(path + '//cInsulin-seq-clean.txt', 'w') as textFile:
    textFile.write(cInsulin)
with open(path + '//aInsulin-seq-clean.txt', 'w') as textFile:
    textFile.write(aInsulin)

# Printing "the sequence of human insulin" to console using successive print() commands:
print('The sequence of human preproinsulin: {}\nTotal of {} characters in this sequence\n'.format(preproInsulin, len(preproInsulin)))
print('The sequence of human insulin, chain ls: sequencing: {}'.format(lsInsulin))
print('The sequence of human insulin, chain b: sequencing: {}'.format(bInsulin))
print('The sequence of human insulin, chain c: sequencing: {}'.format(cInsulin))
print('The sequence of human insulin, chain a: sequencing: {}'.format(aInsulin))
