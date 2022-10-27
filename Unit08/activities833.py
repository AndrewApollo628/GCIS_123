# 8.3.2

# 8.3.3

def swapper(a_list):
    length = len(a_list)
    if length < 2:
        return a_list
    else:
        half = length // 2
        swapped = []
        for index in range(half, length):
            swapped.append(a_list[index])
        for index in range(half):
            swapped.append(a_list[index])
    return swapped

def main():
    print(swapper([]))
    print(swapper([1]))
    print(swapper([4, 5, 6]))
    print(swapper([6, 7, 8, 9, 10, 1, 2, 3, 4, 5]))

main()