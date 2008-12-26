visited_numbers = set()
sequence_lengths = {1: 1}
for i in reversed(range(1, 1000000)):
    # generate the partial sequence starting from i, until it reaches a visited number
    sequence = []
    while True:
        sequence.append(i)
        if i <= 1:
            break
        if i % 2 == 0:
            next = i // 2
        else:
            next = 3*i + 1
        if i in visited_numbers:
            break
        visited_numbers.add(i)
        i = next
    # figure out the whole sequence length for each number in the partial sequence
    last_num = i
    base_length = sequence_lengths[last_num]
    for index, number in enumerate(reversed(sequence)):
        sequence_lengths[number] = base_length + index

max_length = max(sequence_lengths.values())
max_numbers = [n for n, length in sequence_lengths.items() if length == max_length]

print(max_numbers[0])
