def fill_disk(a, len_disk):
    separator = "0"
    while len(a) < len_disk:
        b = []
        for idx in reversed(range(len(a))):
            c = a[idx]
            if c == "0":
                b.append("1")
            else:
                b.append("0")
        a = a + separator + "".join(b)
    return a[0:len_disk]

def chksum(a):
    while True:
        b = []
        for i in range(len(a)):
            if i % 2 != 0:
                continue
            x = a[i]
            y = a[i+1]
            if x == y:
                b.append("1")
            else:
                b.append("0")
        a = "".join(b)
        if len(a) % 2 != 0:
            break
    return a


filled = fill_disk("01111001100111011", 35651584)
print(filled)
print(chksum(filled))

