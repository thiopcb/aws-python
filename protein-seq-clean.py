# Preparing to Analyze Insulin with Python
##########################################
# Exercise 1: Retrieving the protein sequence of human preproInsulin
# The National Center for Biotechnology Information (NCBI) has information on many biological sequences.
# 1. Access NCBI at https://ncbi.nlm.nih.gov.
# 2. Next to the search bar, choose the dropdown menu and select Protein. Next, in the search bar, enter human insulin and choose Search.
# 3. Choose the following search result: insulin [Homo sapiens].
# 4. At the bottom of the search record, copy the insulin sequence, which starts with the word ORIGIN and ends with //.
# 5. Paste the insulin sequence into a file "preproInsulin-seq.txt".
# Bonus: Cleaning preproInsulin-seq.txt programmatically

# Exercise 2: Obtaining the protein sequence of human insulin
filepreproInsulin = open('preproinsulin-seq.txt', 'r') # open and read file to variable
tempText = '' # initialize temperory line text variable
preproInsulin ='' # Store the human preproInsulin sequence in a variable called preproInsulin

# Define character filtering function to omit '1', '6' and whitespaces from line text
def lineReader(line):
    text = ''
    for char in line:
        if char == '1' or char == '6' or char == ' ':
            text = text + ''
        else:
            text += char
    return text

# Read first line from file
readfileLine = filepreproInsulin.readline().lower().strip(' ')

# Loop through the file, line by line until end of line
while readfileLine != '':
    # Check line to ignore key text: 'origin' and '//'
    if readfileLine != 'origin':
        readfileLine = filepreproInsulin.readline().lower().strip(' ')
        tempText = lineReader(readfileLine).strip(' ').strip('\n')
        if readfileLine == '//':
            preproInsulin += ''
        else:
            preproInsulin += tempText
    else:
        break

filepreproInsulin.close() # close working file after cleaning sequence

# Write cleaned sequence to text file, preproInsulin-seq-clean.txt
with open('preproInsulin-seq-clean.txt', 'w') as f:
    f.write(preproInsulin)

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
with open('lsInsulin-seq-clean.txt', 'w') as f:
    f.write(lsInsulin)
with open('bInsulin-seq-clean.txt', 'w') as f:
    f.write(bInsulin)
with open('cInsulin-seq-clean.txt', 'w') as f:
    f.write(cInsulin)
with open('aInsulin-seq-clean.txt', 'w') as f:
    f.write(aInsulin)
