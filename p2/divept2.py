#!python3.9
from collections import defaultdict as dd

with open('input', 'r') as f:
    hoz, depth, aim = 0,0,0
    _pass = lambda: lambda *_: 0
    parsed = [(cmd, int(val)) for cmd, val in (line.split(" ") for line in f)]
    ex = {'hoz'  : dd(_pass, { 'forward' : lambda x: x }), 
          'depth': dd(_pass, { 'forward' : lambda x,y: x*y }), 
          'aim'  : dd(_pass, { 'down'    : lambda x: x,
                               'up'      : lambda x: x*-1 }),}
    for cmd,val in parsed:
        aim,hoz,depth = (
                aim+ex['aim'][cmd](val), 
                hoz+ex['hoz'][cmd](val),
                depth+ex['depth'][cmd](val,aim),
                )
    print(f"ANS := {hoz*depth}")
