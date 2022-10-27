# 8.3.2

def packer():
    return True, 1, "abc", 3.14159

def main():
    packed = packer()
    print(packed)
    w = packed[0]
    x = packed[1]
    y = packed[2]
    z = packed[3]
    print(w)
    print(x)
    print(y)
    print(z)

main()