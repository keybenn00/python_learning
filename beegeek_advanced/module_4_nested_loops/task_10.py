def chunked(seq_letters, num_chunk):
    list_result = []
    list_counter = []

    for i in range(len(seq_letters)):
        list_counter.append(seq_letters[i])
        if len(list_counter) == num_chunk:
            list_result.append(list_counter)
            list_counter = []

    if len(list_counter) != 0:
        list_result.append(list_counter)
        
    return list_result

        
seq_letters = [el for el in input().split()]
num_chunk = int(input())

print(chunked(seq_letters,num_chunk))