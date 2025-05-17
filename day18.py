def is_trap(prev_row, idx):
    left = "." if idx - 1 < 0 else prev_row[idx-1]
    center = prev_row[idx]
    right = "." if idx +1 >= len(prev_row) else prev_row[idx+1]
    return (left == "^" and center == "^" and right == ".") or (right == "^" and center == "^" and left == ".") or (right == "^" and center == "." and left == ".") or (left == "^" and center == "." and right == ".")

input = "^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^"

steps = 0
rows = [input]
while steps < 399999:
    next_row = [] 
    prev_row = rows[len(rows)-1]
    for idx in range(len(prev_row)):
       next_row.append("^" if is_trap(prev_row, idx) else ".") 
    rows.append("".join(next_row))
    steps += 1

safe_tiles = 0
for r in rows:
    for c in r:
        if c == ".":
            safe_tiles += 1

print(safe_tiles)
print(len(rows))
