#Author: Andrew Apollo 

import pick

def test_check_guess_correct():
    out = pick.check_guess(5,5)
    assert (out == 0)

def test_check_guess_incorrect():
    out = pick.check_guess(5,5)
    assert (out >= 0)

def test_check_guess_too_high():
    out = pick.check_guess(11,4)
    assert (out < 0)

def test_check_guess_too_low():
    out = pick.check_guess(0,4)
    assert (out < 0)