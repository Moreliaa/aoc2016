input = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.""".split("\n")
input = open("day15.txt").readlines()
import re
from collections import namedtuple
rx = r"Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+)."
discs = []
Disc = namedtuple('Disc', 'nr numpos time pos')
for i in input:
    m = re.match(rx, i)
    if m != None:
        discs.append(Disc(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))))
    else:
        print("Something")
 
discs.append(Disc(len(discs) + 1, 11, 0, 0))
targetpos = []
for d in discs:
    t = d.numpos - d.nr
    while t < 0:
        t += d.numpos
    targetpos.append(t)
print(targetpos)

curpos = list(map(lambda x: x.pos, discs))
time = 0
while True:
    #print(str(time) + ": " + str(curpos))
    istarget = True 
    for idx in range(len(curpos)):
        if curpos[idx] != targetpos[idx]:
            istarget = False
            break
    if istarget:
        break
    time += 1
    for idx in range(len(curpos)):
        curpos[idx] += 1
        if curpos[idx] >= discs[idx].numpos:
            curpos[idx] = 0
print(time)
