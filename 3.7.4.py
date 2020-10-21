x, y = 0, 0
for i in range(int(input())):
    list = input().split()
    if list[0] == 'север':
        y += int(list[1])
    elif list[0] == 'юг':
        y -= int(list[1])
    elif list[0] == 'восток':
        x += int(list[1])
    elif list[0] == 'запад':
        x -= int(list[1])
print(x, y)
