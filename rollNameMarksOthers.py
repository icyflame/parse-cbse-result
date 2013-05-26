##File number 3
##
##1951 hrs.
##
##parsing the cbse result into a csv.
##
##
##this file will parse the name, roll number, marls in the five subjects
##the percentage and the stream that the student belongs to.

startMarks = [46,59,72,85,98]

startSubjects = [41,54,67,80,93]

filin = open('inputfile','r')

filout = open('out.csv','w')

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

        rollToName[rollNum] = (name,)  ##each item will have a tuple that will contain the marks.

        marks = []
        
        for i in startMarks:

            rollToName[rollNum] += (line[i:i+2],)

            marks.append(int(line[i:i+2]))

        ##FINDING THE PERCENTAGE

        percentage = sum(marks) / 500.0 * 100.0

        rollToName[rollNum] += (str(percentage),)

        ##FINDING THE STREAM

        subjectList = []

        for i in startSubjects:

            subjectList.append(line[i:i+3])

        if '083' in subjectList:

            rollToName[rollNum] += ('COMPUTER SCIENCE',)

        elif '044' in subjectList:

            rollToName[rollNum] += ('BIOLOGY',)

        else:

            rollToName[rollNum] += ('COMMERCE',)        

        

print rollToName

filout.write('Roll Number,Name,Subject1,Subject2,Subject3,Subject4,Subject5,Percentage,Stream\n')

for i in rollToName.keys():

    filout.write(i + ',')   ##will write the roll number

    for j in rollToName[i]:

        filout.write(j + ',')  ##will write all the other elements.

        
    filout.write('\n')

filout.close()
filin.close()
