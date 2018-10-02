import numpy as np
from mandelbrot_3 import calculate


def test_outside():
    """Raises assertion error if the far out complex values does not get
    intensity 1.
    """
    a = calculate(3, 4, 3, 4, (500, 500), 1000)
    assert np.all(a == 1)


def test_inside():
    """Raises assertion error if the complex values inside the mandelbrot set
    does not give intensity 0.
    """
    a = calculate(-0.1, 0, -0.1, 0, (500, 500), 1000)
    assert np.all(a == 0)


if __name__ == "__main__":
    test_outside()
    test_inside()
