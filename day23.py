def run(input):
    a=input
    b=a-1
    while b > 0:
        d=a
        a=0
        c=b

        a+=c*d
        b-=1

    c = 98
    d = 86
    a+=d*c
    print(a)

run(7)
run(12)
