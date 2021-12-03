#!python3.9
with open("input.txt", 'r') as f:

    all_lines = [line.strip('\n') for line in f]
    MAX_BIT_SIZE = len(all_lines[0])
    gamma = ["" for x in range(MAX_BIT_SIZE)]
    epsilon = ["" for x in range(MAX_BIT_SIZE)]
    for _ in range(MAX_BIT_SIZE):
        CMMN = [0,0]
        for line in all_lines:
            if line[_] == '0':
                CMMN[0] += 1
            else:
                CMMN[1] += 1
            gamma[_] = "0" if CMMN[0] > CMMN[1] else "1"
            epsilon[_] = "0" if CMMN[0] < CMMN[1] else "1"
    # answer to pt.1
    print("Answer 1: ", int(''.join(gamma), base=2) *  int(''.join(epsilon), base=2))

    # oxygen generator rating -> most common in each pos
    buff = all_lines
    oxygen, co2 = 0,0
    for _ in range(MAX_BIT_SIZE):
        CMMN = [0,0]
        for line in buff:
            if line[_] == '0':
                CMMN[0] += 1
            else:
                CMMN[1] += 1
        cmp = "1" if CMMN[1] >= CMMN[0] else "0"
        buff = list(filter(lambda x: x[_] == cmp, buff))
    oxygen = (int(''.join(buff), base=2))

    buff = all_lines
    for _ in range(MAX_BIT_SIZE):
        CMMN = [0,0]
        for line in buff:
            if line[_] == '0':
                CMMN[0] += 1
            else:
                CMMN[1] += 1
        cmp = "0" if CMMN[0] <= CMMN[1] else "1"
        if(len(buff) == 1):
            break
        buff = list(filter(lambda x: x[_] == cmp, buff))
    co2 = int(''.join(buff), base=2)
    # answer to pt 2
    print("Answer 2: ", co2 * oxygen)
