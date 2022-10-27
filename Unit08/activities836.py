# 8.3.6

def comprehension():
    print([letter for letter in "foobar"])
    print([0 for _ in range(15)])
    print([number for number in range(13)])
    print([number for number in range(0, 21, 2)])
    print([n for n in range(0, 50) if n % 3 == 0 or n % 5 == 0])

def main():
    comprehension()
    
main()