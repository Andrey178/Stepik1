marksLine = []
avgMark = 0
with open("D:\\Programming\\fileout.txt", 'w') as out:
    out.write('')
with open("D:\\Programming\\dataset_3363_4.txt") as inf:
    for line in inf:
        userList = ['', 0, 0, 0]
        userList = line.strip().split(';')
        for i in range(1, len(userList)):
            userList[i] = int(userList[i])

        avgMark = round(sum(userList[1:])/(len(userList)-1), 9)
        print(userList, avgMark)
        marksLine.append(userList[1:])
        with open("D:\\Programming\\fileout.txt", 'a') as out:
            out.write(str(avgMark)+'\n')
with open("D:\\Programming\\fileout.txt", 'a') as out:
    avgMark = 0
    for i in range(len(marksLine[0])):
        avgMark = 0
        for ii in range(len(marksLine)):
            avgMark += marksLine[ii][i]
        avgMark /= len(marksLine)
        print(avgMark, end=' ')
        out.write(str(str(avgMark)+' '))