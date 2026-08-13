number = input()[::-1]
flag = False

if len(number) == 6:
    remember = number[-1]
    number = remember + number[0:5]

if number[0] == '0':
    for i in range(len(number)):
        if number[i] == '0':
            number = number.replace('0'[i], '')
        else:
            break


print(number)