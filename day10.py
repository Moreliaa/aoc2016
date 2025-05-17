import re
rx = r"value (\d+) goes to bot (\d+)"
rx2 = r"bot (\d+) gives (.+) to (bot|output) (\d+) and (.+) to (bot|output) (\d+)"
input =  open("day10.txt").readlines()
bots = {}
outputs = {}
for i in input: 
    m = re.match(rx, i)
    if m:
        bot = m.group(2)
        v = int(m.group(1))
        if bot in bots:
            bots[bot].append(v)
        else:
            bots[bot] = [v]

while True:
    for i in input: 
        m = re.match(rx2, i)
        if m:
            bot = m.group(1)
            if bot in bots and len(bots[bot]) > 1:
                if min(bots[bot]) == 17 and max(bots[bot]) == 61:
                    print(bot)
                comp1 = m.group(2)
                v1 = min(bots[bot]) if comp1 == "low" else max(bots[bot])
                v2 = max(bots[bot]) if comp1 == "low" else min(bots[bot])
                bots[bot] = []
                bot1 = m.group(4)
                bot2 = m.group(7)
                group1 = bots if m.group(3) == "bot" else outputs
                group2 = bots if m.group(6) == "bot" else outputs
                if bot1 in group1:
                    group1[bot1].append(v1)
                else:
                    group1[bot1] = [v1]
                if bot2 in group2:
                    group2[bot2].append(v2)
                else:
                    group2[bot2] = [v2]
    if "0" in outputs and "1" in outputs and "2" in outputs:
        print(outputs["0"][0] * outputs["1"][0] * outputs["2"][0])
        break
