##File number 2
##
##1930 hrs.
##
##parsing the cbse result into a csv.
##
##
##basic parsing output. it will write to csv the rollnumber,name
##and the marks of the five subjects. with the respective headers.

filin = open('inputfile','r')

filout = open('RollNameAndMarks.csv','w')

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

        startMarks = [46,59,72,85,98]
        
        for i in startMarks:

            rollToName[rollNum] += (line[i:i+2],)        

print rollToName

filout.write('Roll Number,Name,Subject1,Subject2,Subject3,Subject4,Subject5\n')

for i in rollToName.keys():

    filout.write(i + ',')   ##will write the roll number

    for j in rollToName[i]:

        filout.write(j + ',')  ##will write all the elements.

        
    filout.write('\n')

filout.close()
filin.close()
