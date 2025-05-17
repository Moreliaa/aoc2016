pwdlen = 8
index = 0

prefix = "00000"
pwcharidx = 5

input = "ffykfhsq"
#input = "abc"
import hashlib

found_chars = []
#while len(found_chars) < pwdlen:
#    next_input = input + str(index)
#    result = hashlib.md5(bytes(next_input, "utf-8"))
#    md5 = result.hexdigest()
#    if prefix == md5[0:pwcharidx]:
#        found_chars.append(md5[pwcharidx])
#        print("*")
#    index+=1

print("".join(found_chars))
index = 0
found_chars = ["*"] * pwdlen
count = 0
while count < pwdlen:
    result = hashlib.md5()
    result.update((input + str(index)).encode("utf-8"))
    md5 = result.hexdigest()
    if prefix == md5[0:5]:
        pos = int(md5[5], 16)
        if pos < 8:
            if found_chars[pos] == "*":
                found_chars[pos] = md5[6]
                count += 1
                print("".join(found_chars))
    index+=1

print("".join(found_chars))
