# 8.3.5

def sevens_key(value):
    string = str(value)
    if string[0] == "7":
        return 0
    else:
        return 100

def lucky_7s(a_list):
    print(a_list)
    a_list.sort(key=sevens_key)
    print(a_list)

def main():
    my_list = [value for value in range(0,100,7)]
    lucky_7s(my_list)

main()