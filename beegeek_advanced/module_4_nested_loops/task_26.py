values = [int(i) for i in input().split()]

for i in range(values[0]):
    for j in range(values[1]):
        if (i + j) % 2 == 0:
            print('.', end = ' ')
        else:
            print('*', end = ' ')
    print()