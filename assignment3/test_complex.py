from complex import Complex


def test_addition():
    """Raises AssertionError if adding Complex objects does not return
    expected values.
    """
    z = Complex(-5, 3)
    w = Complex(11, -7)
    ans = z + w
    expected = Complex(6, -4)
    assert ans.real == expected.real and ans.imag == expected.imag


def test_subtraction():
    """Raises AssertionError if subtrcting Complex objects does not return
    expected values.
    """
    z = Complex(-5, 3)
    w = Complex(11, -7)
    ans = z - w
    expected = Complex(-16, 10)
    assert ans.real == expected.real and ans.imag == expected.imag


def test_conjugate():
    """Raises AssertionError if conjugating Complex objects does not return
    expected values.
    """
    z = Complex(-5, 3)
    ans = z.conjugate()
    expected = Complex(-5, -3)
    assert ans.real == expected.real and ans.imag == expected.imag


def test_equals():
    """Raises AssertionError if checking the equality of Complex objects does
    not return expected values.
    """
    z = Complex(11, -7)
    w = Complex(11, -7)
    assert z == w
