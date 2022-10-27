# 8.3.4

def chunky(a_list, size):
    start = 0
    stop = size
    chunk = a_list[start:stop]
    while chunk:
        print(chunk)
        start = stop
        stop = start + size
        chunk = a_list[start:stop]

def main():
    chunky([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)

main()