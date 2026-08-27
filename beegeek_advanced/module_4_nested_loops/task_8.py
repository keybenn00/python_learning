def pascal(n):
    current_row = [1]
    for _ in range(n):
        new_row = [1]
        for k in range(len(current_row) - 1):
            new_row.append(current_row[k] + current_row[k + 1])
        new_row.append(1)
        current_row = new_row
    return current_row


n = int(input())

print(pascal(n))