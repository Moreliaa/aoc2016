max_int = 4294967295
input = open("day20.txt").readlines()
bounds = [(0, max_int)]
new_bounds = []
blockers = []
for i in input:
    spl = i.split("-")
    a = int(spl[0])
    b = int(spl[1])
    blockers.append((a,b))

blockers = sorted(blockers, key=lambda x: x[0])
new_blockers = []
idx = 0
while idx < len(blockers):
    bound = blockers[idx]
    a1 = bound[0]
    b1 = bound[1]
    for idx2 in range(idx + 1, len(blockers)):
        bound2 = blockers[idx2]
        a2 = bound2[0]
        if a2 <= b1+1:
            b1 = max(b1, bound2[1])
            idx = idx2
        else:
            break
    idx += 1
    new_blockers.append((a1, b1))
print(new_blockers[0])
print(new_blockers[1])

sum = 0
for idx in range(len(new_blockers)-1):
    bound1 = new_blockers[idx]
    bound2 = new_blockers[idx+1]
    sum += bound2[0] - bound1[1] - 1
print(sum)
