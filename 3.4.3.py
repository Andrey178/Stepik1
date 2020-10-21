import os
def readStringFile():
   inf = open("D:\\Programming\\dataset_3363_3.txt", 'r')
   str = inf.read().lower()
   print(str)
   inf.close()
   return str

def writeStringFile(str):
   with open ("D:\\Programming\\fileout.txt", 'w') as outf:
      outf.write(str)

def countWords(str):
    strMap = {}
    for i in str.split():
        for ii in i.split():
            if ii not in strMap:
                strMap.setdefault(ii, 0)
            if ii in strMap:
                strMap[ii] += 1
#    print(strMap)
    return strMap

def findMax(strMap):
    intMax = 0
    listMax = []
    for i in strMap:
#        print(i, sep=' ')
        if intMax < strMap[i]:
            intMax = strMap[i]
 #   print(intMax)
    for i in strMap:
        if strMap[i] == intMax:
            listMax.append(i)
    listMax.sort()
    print(listMax[0], intMax)

str = readStringFile()
#print (str)
strMap = countWords(str)
strMax = findMax(strMap)
