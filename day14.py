import hashlib
import cProfile

input = "yjdafjpo"
#input = "abc"
index = 0
hashes = []

def make_hash():
    result = hashlib.md5()
    result.update((input + str(index)).encode("utf-8"))
    md5 = result.hexdigest()
    for i in range(2016):
        result = hashlib.md5()
        result.update((md5).encode("utf-8"))
        md5 = result.hexdigest()
    #print(str(index) + ": " + md5)
    hashes.append(md5)
def run():
    global index
    while len(hashes) < 1000:
        make_hash()
        index += 1

    valid_idx = []
    while len(valid_idx) < 64:
        hash = hashes.pop(0)
        make_hash()
        index += 1
        for idx in range(len(hash) - 2):
            a = hash[idx]
            b = hash[idx+1]
            c = hash[idx+2]
            if a == b and b == c:
                for index2 in range(len(hashes)):
                    found = False
                    hash2 = hashes[index2]
                    for idx2 in range(len(hash2) - 4):
                        a2 = hash2[idx2]
                        b2 = hash2[idx2+1]
                        c2 = hash2[idx2+2]
                        d2 = hash2[idx2+3]
                        e2 = hash2[idx2+4]
                        if a2 == a and b2 == a and c2 == a and d2 == a and e2 == a:
                            valid_idx.append(index - 1001)
                            found = True
                            print(str(index - 1001) + ":" + str(index - (len(hashes) - index2)))
                            break
                    if found:
                        break
                break
    print(valid_idx)

cProfile.run("run()")
