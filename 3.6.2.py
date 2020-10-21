import requests
Line = ''

with open("D:\\Programming\\dataset_3378_2.txt") as inf:
    Line = inf.readline().strip()
    print('Got line:', Line)


r = requests.get(Line.strip())
print(r)
print(r.url)
#print(r.headers)
pageStrings = r.text
pageStrings2 = pageStrings.splitlines()
#for i in pageStrings.split('\n'):
#    pageStrings2.append(i)
index = 1
for i, ii in enumerate(pageStrings2, 1):
    print(i)
#    index += 1
#print(pageStrings[0:200])
print('Num strings: ', len(pageStrings2))