import re

swap_pos = r"swap position (\d+) with position (\d+)"
swap_ltr = r"swap letter (\w+) with letter (\w+)"
rot = r"rotate (left|right) (\d+) step"
rot_pos = r"rotate based on position of letter (\w+)"
rev_pos = r"reverse positions (\d+) through (\d+)"
mov_pos = r"move position (\d+) to position (\d+)"

input = open("day21.txt").readlines()
scrambled = list("abcdefgh")
for i in input:
    m = re.match(swap_pos, i)
    m2 = re.match(swap_ltr, i)
    m3 = re.match(rot, i)
    m4 = re.match(rot_pos, i)
    m5 = re.match(rev_pos, i)
    m6 = re.match(mov_pos, i)
    if m:
        x = int(m.group(1))
        y = int(m.group(2))
        a = scrambled[x]
        scrambled[x] = scrambled[y]
        scrambled[y] = a
    elif m2:
        x = m2.group(1)
        y = m2.group(2)
        a = scrambled.index(x)
        b = scrambled.index(y)
        c = scrambled[a]
        scrambled[a] = scrambled[b]
        scrambled[b] = c

    elif m3:
        dir = m3.group(1)
        x = int(m3.group(2))
        if dir == "left":
            for j in range(x):
                p = scrambled.pop(0)
                scrambled.append(p)
        else:
            for j in range(x):
                p = scrambled.pop()
                scrambled.insert(0, p)
    elif m4:
        x = m4.group(1)
        idx = scrambled.index(x)
        if idx >= 4:
            idx += 1
        idx += 1
        for j in range(idx):
            p = scrambled.pop()
            scrambled.insert(0, p)

    elif m5:
        x = int(m5.group(1))
        y = int(m5.group(2))
        while x != y and x < y:
            a = scrambled[x]
            scrambled[x] = scrambled[y]
            scrambled[y] = a
            x += 1
            y -= 1
    elif m6:
        x = int(m6.group(1))
        y = int(m6.group(2))
        a = scrambled[x]
        scrambled.remove(a)
        scrambled.insert(y, a)

    else:
        print(i)
        print("goofed")

print("".join(scrambled))

input = reversed(open("day21.txt").readlines())
scrambled = list("fbgdceah")
for i in input:
    m = re.match(swap_pos, i)
    m2 = re.match(swap_ltr, i)
    m3 = re.match(rot, i)
    m4 = re.match(rot_pos, i)
    m5 = re.match(rev_pos, i)
    m6 = re.match(mov_pos, i)
    if m:
        x = int(m.group(1))
        y = int(m.group(2))
        a = scrambled[x]
        scrambled[x] = scrambled[y]
        scrambled[y] = a
    elif m2:
        x = m2.group(1)
        y = m2.group(2)
        a = scrambled.index(x)
        b = scrambled.index(y)
        c = scrambled[a]
        scrambled[a] = scrambled[b]
        scrambled[b] = c

    elif m3:
        dir = m3.group(1)
        x = int(m3.group(2))
        if dir == "right":
            for j in range(x):
                p = scrambled.pop(0)
                scrambled.append(p)
        else:
            for j in range(x):
                p = scrambled.pop()
                scrambled.insert(0, p)
    elif m4:
        # shift len:
        # 0 1 => 1
        # 1 3 => 2
        # 2 5 => 3
        # 3 7 => 4
        # 4 10 -> 2 => 6
        # 5 12 -> 4 => 7
        # 6 14 -> 6 => 8
        # 7 16 -> 0 => 9
        x = m4.group(1)
        idx = scrambled.index(x)
        idxmap = {1:1,3:2,5:3,7:4,2:6,4:7,6:8,0:9}
        idx = idxmap[idx]
        for j in range(idx):
            p = scrambled.pop(0)
            scrambled.append(p)

    elif m5:
        x = int(m5.group(1))
        y = int(m5.group(2))
        while x != y and x < y:
            a = scrambled[x]
            scrambled[x] = scrambled[y]
            scrambled[y] = a
            x += 1
            y -= 1
    elif m6:
        x = int(m6.group(2))
        y = int(m6.group(1))
        a = scrambled[x]
        scrambled.remove(a)
        scrambled.insert(y, a)

    else:
        print(i)
        print("goofed")

print("".join(scrambled))
