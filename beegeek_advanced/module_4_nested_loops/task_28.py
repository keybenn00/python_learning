values = [int(i) for i in input().split()]
step = 0

for i in range(values[0]):
    for j in range(values[1]):
        step += 1
        print(str(step).ljust(3), end = ' ')
    print()