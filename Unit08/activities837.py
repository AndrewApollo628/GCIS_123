# 8.3.7

def make_table(rows, columns, value):
    # a likely solution
    # table = [[] for _ in range(rows)]
    # for row in table:
    #     row += [value for _ in range(columns)]
    
    # less likely
    table = [[value for _ in range(columns)] for _ in range(rows)]

    for row in table:
        print(row)
    
    return table

def main():
    make_table(3,4,7)
    make_table (10,15,"X")
    
main()