# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

str = [4, -1, 9, 3]
str2 = []
sum = 0
print(len(str))
stri = len(str)
i = 0
while i < stri:
    if i == 0:
        str2.append(str[-1] + str[i + 1])
        elif i == 1:
            str2.append(str[i - 1] + str[0])
        else:
            str2.append(str[i - 1] + str[i + 1])

        print(sum + ' ')
        sum = 0
        i += 1
        print(sum)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
