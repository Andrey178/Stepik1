sum = 3
matchList = ['Спартак;9;Зенит;10', 'Локомотив;12;Зенит;3', 'Спартак;8;Локомотив;15']

#sum = int(input())
teams = {}
for i in range(sum):
#    match = input().split(';')
    match = matchList[i].split(';')
#    print(*match)
    for i in match[0::2]:
        teams.setdefault(i, [0, 0, 0, 0, 0])
    if int(match[1]) > int(match[3]):
        teams[match[0]][0] += 1
        teams[match[2]][0] += 1
        teams[match[0]][1] += 1
        teams[match[2]][3] += 1
        teams[match[0]][4] += 3
    elif int(match[1]) < int(match[3]):
        teams[match[2]][0] += 1
        teams[match[0]][0] += 1
        teams[match[2]][1] += 1
        teams[match[0]][3] += 1
        teams[match[2]][4] += 3
    else:
        teams[match[0]][0] += 1
        teams[match[2]][0] += 1
        teams[match[0]][2] += 1
        teams[match[2]][2] += 1
        teams[match[0]][4] += 1
        teams[match[2]][4] += 1
for i, ii in teams.items():
    print('{}:{} {} {} {} {}'.format(i, *ii))



