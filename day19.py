v = 3012210

def msb(n):
    msb = 0
    n = int(n/2)
    while n > 0:
        n = int(n / 2)
        msb += 1
    return 1 << msb

def pt1(n):
	return 2 * (n - msb(n)) + 1

print(pt1(v))

def pt2(n):
    offset = 1
    while offset * 3 < n:
        offset *= 3
    return n - offset

print(pt2(v))
