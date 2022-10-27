#Author Andrew Apollo 

#Imports
import review02
import arrays 
import array_utils

def test_is_power_1():
    a = 1
    b = 123
    expected = True
    actual = review02.is_power(a,b)

    assert expected == actual

def test_is_power_no_divide():
    a = 10
    b = 3
    expected = False
    actual = review02.is_power(a,b)

    assert expected == actual

def test_is_power_true():
    a = 128
    b = 2
    expected = True
    actual = review02.is_power(a,b)

    assert expected == actual

def test_what_power_1():
    a = 1
    b = 123
    expected = 0
    actual = review02.what_power(a,b)

    assert expected == actual

def test_what_power():
    a = 128
    b = 2
    expected = 7
    actual = review02.what_power(a,b)

    assert expected == actual

def test_what_power_exept():
    a = 30
    b = 3
    
    try:
        review02.what_power(a,b)
        assert False, "value error should be raised"
    except:
        pass

def test_array_equal_0():
    a_array = arrays.Array(0)
    b_array = arrays.Array(0)
    expected = True
    actual = review02.arrays_equal(a_array, b_array)

    assert expected == actual

def test_array_equal_several():
    a_array = array_utils.range_array(1, 11, 2)
    b_array = array_utils.range_array(1, 11, 2)
    expected = True
    actual = review02.arrays_equal(a_array, b_array)

    assert expected == actual

def test_array_equal_diffrent_lengths():
    a_array = array_utils.range_array(1, 11, 2)
    b_array = array_utils.range_array(1, 13, 2)
    expected = False
    actual = review02.arrays_equal(a_array, b_array)

    assert expected == actual

def test_array_equal_diffrent_values():
    a_array = array_utils.range_array(2, 12, 2)
    b_array = array_utils.range_array(1, 11, 2)
    expected = False
    actual = review02.arrays_equal(a_array, b_array)

    assert expected == actual

def test_multiples():
    rows = 2 
    col = 3
    
    table = review02.multiples(rows, col)

    assert table[0][0] == 3
    assert table[0][1] == 2
    assert table[0][2] == 3
    assert table[1][0] == 2
    assert table[1][1] == 4
    assert table[1][2] == 6


