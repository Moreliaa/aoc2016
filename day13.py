open = [(1, 1)]
closed = {}
steps = 0
next_open = []
target = (31, 39)
fav = 1352

#target = (7, 4)
#fav = 10

def tile(x, y):
    a = x*x + 3*x + 2*x*y + y + y*y
    a += fav
    b = a.to_bytes(2, byteorder='big')
    one_bits = 0
    for byte in b:
        one_bits+=((byte>>7)&1)+((byte>>6)&1)+((byte>>5)&1)+((byte>>4)&1) + ((byte>>3)&1)+((byte>>2)&1)+((byte>>1)&1)+(byte&1)

    if one_bits % 2 == 0:
        return "."
    else:
        return "#"

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
open_count = 0
while True:
    finished = False
    for o in open:
        if o in closed:
            continue
        closed[o] = "."
        if steps <= 50:
            open_count += 1
        if o == target:
            print(steps)
            finished = True
            break

        for d in dirs:
            coord = (o[0] + d[0], o[1] + d[1])
            if coord[0] < 0 or coord[1] < 0:
                continue
            if coord in closed:
                continue
            if tile(coord[0], coord[1]) == "#":
                closed[coord] = "#"
                continue
            next_open.append(coord)
    steps += 1
    open = next_open
    next_open = []

    if finished:
        break

print("reachable: " + str(open_count))
print(" 0123456789")
for y in range(7):
    chars = str(y)
    for x in range(10):
        if (x, y) in closed:
            chars += closed[(x, y)]
        else:
            chars += "?"
    print(chars)
