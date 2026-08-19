count_fridges = int(input())
flag_word = 'anton'
virus_fridges = []

for i in range(count_fridges):
    str_fridge = input()
    j = 0
    for letter in str_fridge:
        if letter == flag_word[j]:
            j += 1
            if j == len(flag_word):
                virus_fridges.append(i + 1)
                break

print(*virus_fridges)