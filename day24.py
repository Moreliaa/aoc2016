import heapq
map = list(map(lambda x: list(x), open("day24.txt").readlines()))
#map = list(map(lambda x: list(x), open("day24ex.txt").readlines()))


x_start = 0
y_start = 0
targets = set()
for y in range(len(map)):
    for x in range(len(map[0])):
        c = map[y][x]
        if c == '.' or c == '#' or c == '\n':
            continue
        elif c=='0':
            x_start = x
            y_start = y
        else:
            targets.add((x, y))
targets = frozenset(targets)
print((x_start,y_start))
print(targets)

def astar_nodes(start_pos):
    open = {0: [start_pos] }
    closed = {}
    lowest_steps = [0]
    heapq.heapify(lowest_steps)

    while len(lowest_steps) > 0:
        key = heapq.heappop(lowest_steps)
        states = open[key]
        open[key] = []

        for pos in states:
            if pos in closed:
                continue
            closed[pos] = key

            steps = key+1
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            for d in dirs:
                x = pos[0]+d[0]
                y = pos[1]+d[1]
                c = map[y][x]
                if c == '#':
                    continue
                new_pos = (x,y)
                new_state = new_pos
                if new_state in closed and closed[new_state] <= steps:
                    continue
                if steps in open:
                    open[steps].append(new_state)
                else:
                    open[steps] = [new_state]

                if not lowest_steps.__contains__(steps):
                    heapq.heappush(lowest_steps, steps)
    return closed

distance_map = {}
targets_total = frozenset(targets | set({(x_start,y_start)}))
for start in targets_total:
    distance_map[start] = {}
    closed = astar_nodes(start)
    for end in targets_total:
        distance_map[start][end] = closed[end]


def astar_bot(targets, distance_map, ispt2):
    open = {0: [((x_start, y_start), targets)]}
    closed = {}
    lowest_steps = [0]
    heapq.heapify(lowest_steps)

    pt2_results = []
    heapq.heapify(pt2_results)
    while len(lowest_steps) > 0:
        key = heapq.heappop(lowest_steps)
        states = open[key]
        open[key] = []
        finished = False

        for s in states:
            pos = s[0]
            t = s[1]
            if len(t)==0:
                if not ispt2:
                    print(key)
                    finished = True
                    break
                else:
                    last = (x_start, y_start)
                    steps = key+distance_map[pos][last]
                    heapq.heappush(pt2_results, steps)
                    continue

            closed[s] = key

            dirs = t
            
            for d in dirs:
                steps = key+distance_map[pos][d]
                new_pos = d 
                new_t = t if not t.__contains__(new_pos) else frozenset(t - set({(new_pos)}))
                new_state = (new_pos, new_t)
                if new_state in closed and closed[new_state] <= steps:
                    continue
                if steps in open:
                    open[steps].append(new_state)
                else:
                    open[steps] = [new_state]

                if not lowest_steps.__contains__(steps):
                    heapq.heappush(lowest_steps, steps)
        if finished:
            break
    if ispt2:
        return heapq.heappop(pt2_results)


print(distance_map)
astar_bot(targets, distance_map, False)
print(astar_bot(targets, distance_map, True))
