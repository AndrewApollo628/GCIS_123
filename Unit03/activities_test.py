#Author: Andrew Apollo

def test_square_area_8():
    area = square_area(8)
    assert (area == 64)

def test_square_area_6():
    area = square_area(6)
    assert (area == 36)

def test_square_area_neg6():
    area = square_area(-6)
    assert (area == "none")

def square_area(length):
    if length < 0:
        return "none"
    return length * length
