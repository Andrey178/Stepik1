import requests

Linebase = 'https://stepic.org/media/attachments/course67/3.6.3/'
Line = ''
tryMore = True

with open("D:\\Programming\\dataset_3378_3.txt") as inf:
    Line = inf.readline().strip()
    print('Got line:', Line)

while tryMore:
    r = requests.get(Line).text
    if r[:2] == 'We':
        print(r)
        break
    else:

        print(r)
        Line = Linebase+r