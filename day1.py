input = "L1, L5, R1, R3, L4, L5, R5, R1, L2, L2, L3, R4, L2, R3, R1, L2, R5, R3, L4, R4, L3, R3, R3, L2, R1, L3, R2, L1, R4, L2, R4, L4, R5, L3, R1, R1, L1, L3, L2, R1, R3, R2, L1, R4, L4, R2, L189, L4, R5, R3, L1, R47, R4, R1, R3, L3, L3, L2, R70, L1, R4, R185, R5, L4, L5, R4, L1, L4, R5, L3, R2, R3, L5, L3, R5, L1, R5, L4, R1, R2, L2, L5, L2, R4, L3, R5, R1, L5, L4, L3, R4, L3, L4, L1, L5, L5, R5, L5, L2, L1, L2, L4, L1, L2, R3, R1, R1, L2, L5, R2, L3, L5, L4, L2, L1, L2, R3, L1, L4, R3, R3, L2, R5, L1, L3, L3, L3, L5, R5, R1, R2, L3, L2, R4, R1, R1, R3, R4, R3, L3, R3, L5, R2, L2, R4, R5, L4, L3, L1, L5, L1, R1, R2, L1, R3, R4, R5, R2, R3, L2, L1, L5"
input_split = input.split(", ");
current_dir = 0
x = 0
y = 0
seen_set = {"0,0": 1}

x_pt2 = 0
y_pt2 = 0

for i in input_split:
   dir = i[0]
   times = int(i[1:])
   if dir == "L":
       current_dir = current_dir - 1
       if current_dir < 0:
           current_dir = 3
   else:
        current_dir = current_dir + 1
        if current_dir > 3:
            current_dir = 0
   while times > 0:
       times -= 1
       if current_dir == 0: #n
            y += 1
       elif current_dir == 1: #e
            x += 1
       elif current_dir == 2: #s
            y -= 1
       else: #w
            x -= 1
       key = str(x) + "," + str(y)
       if x_pt2 == 0 and y_pt2 == 0 and key in seen_set:
           x_pt2 = x
           y_pt2 = y
       else:
           seen_set[key] = 1

print(x)
print(y)
print(abs(x)+abs(y))
print(x_pt2)
print(y_pt2)
print(abs(x_pt2)+abs(y_pt2))
