dicClasses = {}
with open('D:\\Programming\\dataset_3380_5.txt') as inf:
    for i in inf.readlines():
        list = i.strip().split('\t')
        for i in range(len(list)):
            if list[i].isdigit():
                list[i] = int(list[i])
        if list[0] not in dicClasses:
            dicClasses.setdefault(list[0], [0, 0])
        dicClasses.get(list[0])[1] += list[2]
        dicClasses.get(list[0])[0] += 1

#print(dicClasses, '!')

for i in range(1, 12):
    print(i, dicClasses.get(i)[1]/dicClasses.get(i)[0] if i in dicClasses else '-')