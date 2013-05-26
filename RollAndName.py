##File number 1
##
##1914 hrs.
##
##parsing the cbse result into a csv.
##
##This file will parse the rollnumbers and the names.
##What it does is that it creates a csv file which will
##have to headers. roll number and name.
##
##the marks of the student will not be shown.

filin = open('inputfile','r')

filout = open('RollAndName.csv','w')

rollToName = {}

for line in filin:

    if not line[0] == str(4):

        continue

    else:

        startRoll = 0
        endRoll = line.find(' ')
        startName = endRoll + 1
        endName = line.find(' ',line.find('  ') + 1)

        rollNum = line[startRoll:endRoll]
        name = line[startName:endName - 1]

        rollToName[rollNum] = name

print rollToName

filout.write('Roll Number,Name\n')

for i in rollToName.keys():

    filout.write(i + ',' + rollToName[i] + '\n')


filout.close()
filin.close()
