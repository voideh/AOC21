#!python3.9
# original solution -- too much code!
def gen_indices(n):
    return set(max(n-x, 0) for x in range(3))

with open('input', 'r') as f:
    sums = list()
    counter = 0
    for line in f:
        content = int(line.strip('\n'))
        indices = gen_indices(counter)
        for i in indices:
            try:
                sums[i] += content
            except:
                sums.append(content)
        counter += 1

    prev = 0
    total = 0
    for s in sums:
        if prev != 0 and s > prev:
            total += 1
        prev = s
    print(total)
