import hashlib
import random
index = 0
password = '________'
while 1:
    m = hashlib.md5()
    m.update(('ffykfhsq'+str(index)).encode('utf-8'))
    hex_m = m.hexdigest()
    if hex_m[0:5] == '00000':
        password_pos = int(hex_m[5], 16)
        if password_pos < 8:
            password_dig = int(hex_m[6], 16)
            if password[password_pos] == '_':
                password = password[:password_pos] + hex(password_dig)[-1] + password[password_pos + 1:]
    if index % 30000 == 0:
        for char in password:
            if char == '_':
                print(str(random.random())[-1], end='')
            else:
                print(char, end='')
        print('\r', end='')
    index += 1
