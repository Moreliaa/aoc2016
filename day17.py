import hashlib
input = [
  "#########",
  "#S| | | #",
  "#-#-#-#-#",
  "# | | | #",
  "#-#-#-#-#",
  "# | | | #",
  "#-#-#-#-#",
  "# | | |  ",
  "####### V",
]

start_state = (1, 1, "pvhmgsws")
dirs =[(0, -1, "U"), (0, 1, "D"), (-1, 0, 'L'), (1, 0, 'R')]
chars_open = {'b','c','d','e','f'}

open = [start_state]
next_open = []
steps = 0
while True:
    for o in open:
        if o[0] == 7 and o[1] == 7:
            print("SUCCESS")
            print(str(steps) + ": " + o[2])
            continue

        result = hashlib.md5()
        result.update((o[2]).encode("utf-8"))
        md5 = result.hexdigest()

        for d in dirs:
            x = o[0] + d[0]
            y = o[1] + d[1]
            if x >= len(input[0]) or y >= len(input):
                continue
            tile = input[y][x]
            if tile == "#":
                continue
            idx = dirs.index(d)
            is_open = chars_open.__contains__(md5[idx])
            if not is_open:
                continue
            next_o = (o[0] + d[0]*2, o[1] + d[1]*2, o[2]+d[2])
            next_open.append(next_o)

    if len(open) == 0:
        break
    open = next_open
    next_open = []
    steps += 1

