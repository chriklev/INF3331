import math


class Complex:
    """Object for storing and manipulating complex numbers.

    Args:
        real (float): Real part of the complex number.
        imag (float): Imaginary part of the complex number.

    Attributes:
        real
        imag

    """

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Assignment 3.3

    def conjugate(self):
        """Returns the conjugate of the complex number it is called from.

        Returns:
            Complex: The conjugate of the object called from.

        """
        return Complex(self.real, self.imag * -1)

    def modulus(self):
        """Returns the modulus of the complex number it is called from.

        Returns:
            Complex: The modulus of the object called from.

        """
        return math.sqrt(self.real**2 + self.imag**2)

    def __add__(self, other):
        """Returns the added value of the complex number called from and the
        complex number given.

        Args:
            other (Complex): The complex number to be added.

        Returns:
            Complex: Added value of complex number called from and given.

        """
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """Returns the given complex number subtracted from the number caled
        from.

        Args:
            other (Complex): The complex number to be subtracted.

        Returns:
            Complex: Result of subtracting given complex number from the number
            called from.

        """
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        """Returns the multiple of the given and the called from complex
        number.

        Args:
            other (Complex): Complex number to be multiplied.

        Returns:
            type: Returns the product of given number and number called from.

        """
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __eq__(self, other):
        """Short summary.

        Args:
            other (type): Description of parameter `other`.

        Returns:
            type: Description of returned object.

        """
        return self.real == other.real and self.imag == other.imag

    def __str__(self):
        """Allows the object to be called as a string.

        Returns:
            String: String representation of the complex number

        """
        return "%.2f+%.2fi" % (self.real, self.imag)

    # Assignment 3.4
    def __radd__(self, other):
        pass

    def __rmul__(self, other):
        pass

    # Optional, possibly useful methods

    # Allows you to write `-a`

    def __neg__(self):
        pass

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        pass
