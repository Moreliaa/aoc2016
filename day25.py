def tryit(input):
    d = input + 11*231

    idx = 0
    a = d
    while a != 0: 
        b = a % 2
        a = int(a / 2) if a % 2 == 0 else int(a/2) 
        if idx % 2 != 0 and b % 2 == 0:
            return False
        elif idx % 2 == 0 and b % 2 != 0:
            return False
        idx+=1
    return True

a = 1
while not tryit(a):
    a += 1
print(a)
