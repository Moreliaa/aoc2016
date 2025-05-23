import re
import copy
import json
import heapq

rx = r"^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T"

input = open("day22.txt").readlines()
#input = open("day22_example.txt").readlines()
nodes = {}

x_t = 0
y_max = 0
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
        avail = size - used
        nodes[(x,y)] = (size, used, avail)

val = list(nodes.values())
pairs = 0
for v in range(len(val)):
    n = val[v]
    used = n[1]
    if used != 0:
        pairs += len(list(filter(lambda x: x != n and used <= x[2], val)))

print(pairs)

for y in range(y_max+1):
    c = []
    for x in range(x_t+1):
        c.append((x,y))
    #print(" ".join(map(lambda x: str(nodes[x][0]) + "/" + str(nodes[x][1]), c)))
print(nodes[(0,0)])
print(nodes[(x_t,0)])
print("max: " + str(x_t) +","+ str(y_max))
target_pairs = list(map(lambda x: nodes[x][0] >= nodes[(x_t,0)][1], nodes))
print(len(target_pairs))

def get_adjacent_pairs(cnodes, n, tar):
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    pairs = []
    n_is_target = n == tar
    for d in dirs:
        p = (n[0] + d[0], n[1] + d[1])
        if p in nodes:
            if n_is_target:
                if p != n and cnodes[n][1] <= cnodes[p][2] and cnodes[p][1] == 0:
                    pairs.append(p)
            else:
                if p != n and cnodes[n][1] <= cnodes[p][2]:
                    pairs.append(p)
    return pairs

def manh(tar):
    return tar[0] + tar[1]

def create_json(state):
    mapped = {}
    for x in state[1]:
        key = str(x[0])+","+str(x[1])
        val = str(state[1][x][0])+","+str(state[1][x][1])+","+str(state[1][x][2])
        mapped[key] = val

    d = json.dumps(mapped, sort_keys=True)
    return str(state[0]) + "," + d + "," + str(state[2])

tar = (x_t, 0)
start_dist = manh(tar)
minh = [start_dist]
heapq.heapify(minh)
open = { start_dist: [(tar, nodes, 0)] }
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
        jsn = create_json(s)
        if jsn in closed and closed[jsn] <= steps:
            continue
        closed[jsn] = steps

        if ctar == (0,0):
            print("Steps: " + str(steps))
            finished = True
            break

        new_steps = steps + 1
        for n in cnodes:
           pairs = get_adjacent_pairs(cnodes, n, ctar)
           for p in pairs:
                new_tar = ctar if n != ctar else p
                new_nodes = copy.deepcopy(cnodes)
                source_node = cnodes[n]
                target_node = cnodes[p]
                new_nodes[n] = (source_node[0], 0, source_node[0])

                p_used = source_node[1] + target_node[1]
                new_nodes[p] = (target_node[0], p_used, target_node[0] - p_used)
                new_state = (new_tar, new_nodes, new_steps) 
                h = manh(new_tar) + new_steps
                if h in open:
                    open[h].append(new_state)
                else:
                    open[h] = [new_state]

                if not minh.__contains__(h):
                    heapq.heappush(minh, h)

    if finished:
        break

