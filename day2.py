instr = """ULL
RRDDD
LURDL
UUUUD""".split("\n")

instr = """LDUDDRUDRRURRRRDRUUDULDLULRRLLLUDDULRDLDDLRULLDDLRUURRLDUDDDDLUULUUDDDDLLLLLULLRURDRLRLRLLURDLLDDUULUUUUDLULLRLUUDDLRDRRURRLURRLLLRRDLRUDURRLRRRLULRDLUDRDRLUDDUUULDDDDDURLDULLRDDRRUDDDDRRURRULUDDLLRRDRURDLLLLLUUUDLULURLULLDRLRRDDLUDURUDRLRURURLRRDDLDUULURULRRLLLDRURDULRDUURRRLDLDUDDRLURRDRDRRLDLRRRLRURDRLDRUDLURRUURDLDRULULURRLDLLLUURRULUDDDRLDDUDDDRRLRDUDRUUDDULRDDULDDURULUDLUDRUDDDLRRRRRDLULDRLRRRRUULDUUDRRLURDLLUUDUDDDLUUURDRUULRURULRLLDDLLUDLURRLDRLDDDLULULLURLULRDLDRDDDLRDUDUURUUULDLLRDRUDRDURUUDDLRRRRLLLUULURRURLLDDLDDD
DRURURLLUURRRULURRLRULLLURDULRLRRRLRUURRLRRURRRRUURRRLUDRDUDLUUDULURRLDLULURRLDURLUUDLDUDRUURDDRDLLLDDRDDLUUDRDUDDRRDLDUDRLDDDRLLDDLUDRULRLLURLDLURRDRUDUDLDLULLLRDLLRRDULLDRURRDLDRURDURDULUUURURDLUDRRURLRRLDULRRDURRDRDDULLDRRRLDRRURRRRUURDRLLLRRULLUDUDRRDDRURLULLUUDDRLDRRDUDLULUUDRDDDDLRLRULRLRLLDLLRRDDLDRDURRULLRLRRLULRULDDDRDRULDRUUDURDLLRDRURDRLRDDUDLLRUDLURURRULLUDRDRDURLLLDDDRDRURRDDRLRRRDLLDDLDURUULURULRLULRLLURLUDULDRRDDLRDLRRLRLLULLDDDRDRU
URUUDUDRDDRDRRRDLLUDRUDRUUUURDRRDUDUULDUDLLUDRRUDLLRDLLULULDRRDDULDRLDLDDULLDDRDDDLRLLDLLRDUUDUURLUDURDRRRRLRRLDRRUULLDLDLRDURULRURULRRDRRDDUUURDURLLDDUUDLRLDURULURRRDRRUUUDRDDLRLRRLLULUDDRRLRRRRLRDRUDDUULULRRURUURURRLRUDLRRUUURUULLULULRRDDULDRRLLLDLUDRRRLLRDLLRLDUDDRRULULUDLURLDRDRRLULLRRDRDLUURLDDURRLDRLURULDLDRDLURRDRLUUDRUULLDRDURLLDLRUDDULLLLDLDDDLURDDUDUDDRLRDDUDDURURLULLRLUDRDDUDDLDRUURLDLUUURDUULRULLDDDURULDDLLD
LRRLLRURUURRDLURRULDDDLURDUURLLDLRRRRULUUDDLULLDLLRDLUDUULLUDRLLDRULDDURURDUUULRUDRLLRDDDURLRDRRURDDRUDDRRULULLLDLRLULLDLLDRLLLUDLRURLDULRDDRDLDRRDLUUDDLURDLURLUDLRDLDUURLRRUULDLURULUURULLURLDDURRURDRLUULLRRLLLDDDURLURUURLLLLDLLLUDLDLRDULUULRRLUUUUDLURRURRULULULRURDDRRRRDRUDRURDUDDDDUDLURURRDRRDRUDRLDLDDDLURRRURRUDLDURDRLDLDLDDUDURLUDUUDRULLRLLUUDDUURRRUDURDRRUURLUDRRUDLUDDRUUDLULDLLDLRUUDUULLDULRRLDRUDRRDRLUUDDRUDDLLULRLULLDLDUULLDRUUDDUDLLLLDLDDLDLURLDLRUUDDUULLUDUUDRUDLRDDRDLDRUUDUDLLDUURRRLLLLRLLRLLRLUUDULLRLURDLLRUUDRULLULRDRDRRULRDLUDDURRRRURLLRDRLLDRUUULDUDDLRDRD
DDLRRULRDURDURULLLLRLDDRDDRLLURLRDLULUDURRLUDLDUDRDULDDULURDRURLLDRRLDURRLUULLRUUDUUDLDDLRUUDRRDDRLURDRUDRRRDRUUDDRLLUURLURUDLLRRDRDLUUDLUDURUUDDUULUURLUDLLDDULLUURDDRDLLDRLLDDDRRDLDULLURRLDLRRRLRRURUUDRLURURUULDURUDRRLUDUDLRUDDUDDRLLLULUDULRURDRLUURRRRDLLRDRURRRUURULRUDULDULULUULULLURDUDUDRLDULDRDDULRULDLURLRLDDDDDDULDRURRRRDLLRUDDRDDLUUDUDDRLLRLDLUDRUDULDDDRLLLLURURLDLUUULRRRUDLLULUUULLDLRLDLLRLRDLDULLRLUDDDRDRDDLULUUR""".split("\n")

keys = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
x = 1
y = 1
pressed = []
for i in instr:
    for c in i:
        if c == "U":
            y = max(0, y - 1)
        elif c == "D":
            y = min(2, y + 1)
        elif c == "L":
            x = max(0, x - 1)
        elif c == "R":
            x = min(2, x + 1)
    pressed.append(keys[y][x])
print("".join(pressed))


def get_dim(xy):
    return 5 - abs(2 - xy) * 2


keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D"]
keys =  [
        [".", ".", "1", ".", "."],
        [".", "2", "3", "4", "."],
        ["5", "6", "7", "8", "9"],
        [".", "A", "B", "C", "."],
        [".", ".", "D", ".", "."],
        ]

x = 0
y = 2
pressed = []
for i in instr:
    for c in i:
        if c == "U":
            next_width = get_dim(y - 1)
            if abs(2 - x) * 2 + 1 <= next_width:
                y = max(0, y - 1)
        elif c == "D":
            next_width = get_dim(y + 1)
            if abs(2 - x) * 2 + 1 <= next_width:
                y = min(4, y + 1)
        elif c == "L":
            next_height = get_dim(x - 1)
            if abs(2 - y) * 2 + 1 <= next_height:
                x = max(0, x - 1)
        elif c == "R":
            next_height = get_dim(x + 1)
            if abs(2 - y) * 2 + 1 <= next_height:
                x = min(4, x + 1)
    pressed.append(keys[y][x])
print("".join(pressed))
