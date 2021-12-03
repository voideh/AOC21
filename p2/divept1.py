#!python3.9
# forward = +x
# down = +y 
# up = -y
hoz = 0
depth = 0
aim = 0

def execute_cmd(direction, amt):
    global hoz
    global depth
    if direction == 'forward':
        hoz += amt
        return
    if direction == 'down':
        depth += amt
        return
    else:
        depth -= amt
        return



with open('input', 'r') as f:
    for line in f:
        direction, magnitude = line.strip('\n').split(' ')
        execute_cmd(direction, int(magnitude))

    print(hoz * depth) # pt 1 solution





