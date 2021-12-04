#!python3.9
vals = list()
# parse input
with open('input', 'r') as f:
    vals = [int(line.strip('\n')) for line in f]

# pt.1
total = len([x for i,x in enumerate(vals[:-1]) if x < vals[i+1]])
print(f"pt1\nANS:={total}")

# pt.2
sums = [sum(vals[0:3])]
total, start, end = 0,1,3
while end < len(vals):
    sums.append(sum(vals[start:end+1]))
    total += 1 if sums[-1] > sums[-2] else 0
    start, end = start+1, end+1
print(f"pt2\nANS:={total}")
