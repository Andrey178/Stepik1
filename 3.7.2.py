#orig, coded, tocode, todecode = input(), input(), input(), input()
orig, coded, tocode, todecode = 'abcd', '*d%#', 'abacabadaba', '#*%*d*%'
print(orig, coded, tocode, todecode)


for i in tocode:
    print(coded[orig.find(i)], end='')
print()
for i in todecode:
    print(orig[coded.find(i)], end='')
print()

print(''.join(i+i for i in tocode))


# for i in tocode:
#    print(i, ' ')
#    print(orig[coded.find(i)-1], '', end='')