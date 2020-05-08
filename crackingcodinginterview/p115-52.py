import struct
def binary(num):
    a =  ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))
    if len(a)>32:
        print("ERROR")
    else:
        print(a)