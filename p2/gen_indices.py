#!python3.9
def gen_indices(n):
    return list(filter(lambda x : x >= 0, [n - x for x in range(3)]))

with open('input', 'r') as f:
    sums = list()
    counter = 0
    for line in f:
        content = int(line.strip('\n'))
        indices = gen_indices(counter)
        for i in indices:
            try:
                print(f'Value {content} added to {i}')
                sums[i] += content
            except:
                print(f'No value @ {i}, inserting {content}')
                sums.append(content)
        counter += 1

    prev = 0
    total = 0
    for s in sums:
        if prev != 0 and s > prev:
            total += 1
        prev = s

    print(total)


