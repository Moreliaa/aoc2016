import re
import heapq

rx = r"^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T"

input = open("day22.txt").readlines()
#input = open("day22_example.txt").readlines()
nodes = {}

x_t = 0
y_max = 0
y_empty = 0
x_empty = 0
for i in input:
    m = re.match(rx, i)
    if m != None:
        x = int(m.group(1))
        if x > x_t:
            x_t = x

        y = int(m.group(2))
        if y > y_max:
            y_max = y
        size = int(m.group(3))
        used = int(m.group(4))
        if used == 0:
            x_empty = x
            y_empty = y
        avail = size - used
        nodes[(x,y)] = (size, used, avail)

val = list(nodes.values())
pairs = 0
for v in range(len(val)):
    n = val[v]
    used = n[1]
    if used != 0:
        pairs += len(list(filter(lambda x: x != n and used <= x[2], val)))

empty_size = nodes[(x_empty,y_empty)][0]
for y in range(y_max + 1):
    c = []
    for x in range(x_t +1):
        n = nodes[(x,y)]
        if n[1] > empty_size:
            c.append("#####")
        else:
            c.append(str(n[1])+"/"+str(n[0]))

    print(" ".join(c))

        
print(nodes[(x_empty,y_empty)])

print(pairs)

print(nodes[(0,0)])
print(nodes[(x_t,0)])
print("max: " + str(x_t) +","+ str(y_max))
target_pairs = list(map(lambda x: nodes[x][0] >= nodes[(x_t,0)][1], nodes))
print(len(target_pairs))

def get_adjacent_pairs(cnodes, n):
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    pairs = []
    for d in dirs:
        p = (n[0] + d[0], n[1] + d[1])
        if p in nodes:
                if p != n and cnodes[n][1] <= empty_size:
                    pairs.append(p)
    return pairs

def manh(tar):
    return tar[0] + tar[1]

def create_json(state):
    return str(state[0]) + "," + str(state[3])

tar = (x_t, 0)
start_dist = manh(tar)
minh = [start_dist]
heapq.heapify(minh)
open = { start_dist: [(tar, nodes, 0, (x_empty, y_empty))] }
closed = {} 

while True:
    key = heapq.heappop(minh)
    print(str(key) + " | " + str(len(minh)))
    states = open[key]
    open[key] = []
    finished=False

    for s in states:
        ctar = s[0]
        cnodes = s[1]
        steps = s[2]
        empty =s[3]
        jsn = create_json(s)
        if jsn in closed and closed[jsn] <= steps:
            continue
        closed[jsn] = steps

        if ctar == (0,0):
            print("Steps: " + str(steps))
            finished = True
            break

        new_steps = steps + 1

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        en = filter(lambda x: x[0] >= 0 and x[0] <= x_t and x[1] >= 0 and x[1] <= y_max, map(lambda x: (empty[0]+x[0],empty[1]+x[1]), dirs))

        for n in en:
           pairs = get_adjacent_pairs(cnodes, n)
           for p in pairs:
                if p != empty:
                    continue
                new_tar = ctar if n != ctar else p

                new_state = (new_tar, nodes, new_steps, n) 
                h = manh(new_tar) + new_steps
                if h in open:
                    open[h].append(new_state)
                else:
                    open[h] = [new_state]

                if not minh.__contains__(h):
                    heapq.heappush(minh, h)

    if finished:
        break

