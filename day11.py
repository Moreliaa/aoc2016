# 1 elevator
# 4 floors
# max elevator capacity: you + 2 chips/RTG
# min elevator capacity: 1 chips/RTG
# stops on each floor (triggers radiation)
# rtg + chip are automatically connected when on the same floor
# start on first floor
# move every item to the fourth floor
# find the minimum number of steps
input = [
   "The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.",
   "The second floor contains a hydrogen generator.",
   "The third floor contains a lithium generator.",
   "The fourth floor contains nothing relevant."
]
input = open("./day11.txt").readlines()
input.append("The first floor contains a elerium-compatible microchip and a dilithium-compatible microchip.")
input.append("The first floor contains a elerium generator and a dilithium generator.")
start_state = {
    "e": "first",
    "first": [], 
    "second": [],
    "third": [],
    "fourth": []
}
import re
import json
import itertools
import copy
import cProfile

rx_floor = r"The (.+) floor"
rx_chip = r"(\w+)-compatible microchip"
rx_gen = r"(\w+) generator"
for i in input:
    floor = re.match(rx_floor, i)
    if floor == None:
        print("Something happened")
        break
    floor = floor.group(1)
    m_chip = re.findall(rx_chip, i)
    for m in m_chip:
        start_state[floor].append(("chip", m))
    m_gen = re.findall(rx_gen, i)
    for m in m_gen:
        start_state[floor].append(("gen", m))

floors = ["first","second","third","fourth"]
for f in floors:
    start_state[f] = sorted(start_state[f])
states = {}

def is_valid(last_state):
    if len(last_state[last_state["e"]]) == 0:
        return False
    for f in floors:
       gens = list(map(lambda g: g[1], filter(lambda g: g[0] == "gen", last_state[f])))
       if len(gens) == 0:
            continue
       chips= list(map(lambda g: g[1], filter(lambda g: g[0] == "chip", last_state[f])))
       for c in chips:
           if c not in gens:
                return False
    return True


def is_finish(last_state):
    for f in floors:
        if f == "fourth":
            continue
        if len(last_state[f]) > 0:
            return False
    return True

def get_next_states(last_state):
    current_floor = last_state["e"]
    current_floor_idx = floors.index(current_floor)
    next_floor_idx_1 = current_floor_idx + 1
    next_floor_idx_2 = current_floor_idx - 1
    next_floors = []
    output = []
    items = last_state[current_floor]
    if next_floor_idx_1 < len(floors):
        next_floor = floors[next_floor_idx_1]
        if len(items) > 1:
            for p in itertools.permutations(items, 2):
                new_state = copy.deepcopy(last_state)
                new_state["e"] = next_floor
                new_state[current_floor] = sorted(filter(lambda i: i not in p, items))
                new_state[next_floor] += p
                if is_valid(new_state):
                    output.append(new_state)
        if len(output) == 0:
            for p in items:
                new_state = copy.deepcopy(last_state)
                new_state["e"] = next_floor
                new_state[current_floor] = sorted(filter(lambda i: i != p, items))
                new_state[next_floor].append(p)
                if is_valid(new_state):
                    output.append(new_state)

    if next_floor_idx_2 >= 0:
        next_floor = floors[next_floor_idx_2]
        for p in items:
            new_state = copy.deepcopy(last_state)
            new_state["e"] = next_floor
            new_state[current_floor] = sorted(filter(lambda i: i != p, items))
            new_state[next_floor].append(p)
            if is_valid(new_state):
                output.append(new_state)
        if len(output) == 0 and len(items) > 1:
            for p in itertools.permutations(items, 2):
                new_state = copy.deepcopy(last_state)
                new_state["e"] = next_floor
                new_state[current_floor] = sorted(filter(lambda i: i not in p, items))
                new_state[next_floor] += p
                if is_valid(new_state):
                    output.append(new_state)

    return output


def run():
    open = [start_state]
    next_open = []
    is_finished = False
    steps = 0
    closed = {}
    def make_hash_2(s, steps):
        eq_state = {
            "e": s["e"],
        }
        for f in floors:
            gens = list(map(lambda x: x[1], filter(lambda x: x[0] == 'gen', s[f])))
            chips = list(map(lambda x: x[1], filter(lambda x: x[0] == 'chip', s[f])))
            count_gens = len(gens)
            count_chips = len(chips)
            pairs = min(count_chips, count_gens)
            singles = abs(count_chips - count_gens)
            if singles == 0:
                eq_state[f] = (pairs, [], [])
            else:
                single_chips = sorted(filter(lambda x: x not in gens, chips))
                single_gens = sorted(filter(lambda x: x not in chips, gens)) 
                eq_state[f] = (pairs, single_chips, single_gens)
                       
        md5 = json.dumps(eq_state)
        if md5 in closed:
            return False
        else:
            closed[md5] = steps
            return True

    while not is_finished:
        print(str(steps) + "...")
        for state in open:
            if not make_hash_2(state, steps):
                continue
            if is_finish(state):
                is_finished = True
                print("Done!")
                break
            next_open += get_next_states(state)
        open = next_open
        next_open = []
        steps += 1
cProfile.run("run()")
