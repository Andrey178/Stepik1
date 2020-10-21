import os
def readStringFile():
   inf = open("D:\\Programming\\dataset_3363_2.txt", 'r')
   str = inf.readline().strip()
   inf.close()
   return str

def writeStringFile(str):
   with open ("D:\\Programming\\fileout.txt", 'w') as outf:
      outf.write(str)

str2 = ''
strnum = ''
strint = 0

str = readStringFile()

i = len(str) - 1
while i >= 0:
   if str[i].isdigit():
      strnum = str[i] + strnum
      i -= 1

   if str[i].isalpha():
      strint = int(strnum)
      strnum = ''
      str2 += str[i]*strint
      i -= 1
#print(len(str2))
str2 = str2[::-1]
writeStringFile(str2)
print(str2)
#print(' '.join(reversed(str2)))