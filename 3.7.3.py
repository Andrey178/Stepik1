import timeit
sumwords = 4
listWords = ['champions', 'we', 'are', 'Stepik']
listErrors = []
numlines = 3
line = ['We are the champignons', 'We Are The Champions', 'Stepic']

#listWords = [input().lower() for i in range(int(input()))]
#print(*listWords)
#for i in line:
#for i in range(int(input())):
for i in line:
    for ii in i.lower().split():
        if ii not in listWords:
            listErrors.append(ii)
print(*set(listErrors), sep='\n')
