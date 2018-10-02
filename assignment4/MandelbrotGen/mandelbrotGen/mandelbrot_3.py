import numpy as np
from numba import jit


@jit(nopython=True)
def calculate(realMin, realMax, imagMin, imagMax,
              resolution, iterations, x_0=0):
    """Computes an array of intensity values for a given rectangle and
    resolution in the mandelbrot set using numba.jit for efficiency.

    Args:
        realMin (float): Minimum value of the real part.
        realMax (float): Maximum value of the real part.
        imagMin (float): Minimum value of the imaginary part.
        imagMax (float): Maximum value of the imaginary part.
        resolution (tuple): Tuple containg two integer values giving the height
                            and width of the picture to generate in pixels.
        iterations (int): Number of iterations before the divirgence-check
                          gives up and assumes convergence.
        x_0 (complex): Initial value for the sequence. Could have hard coded in
                       the value, but cant hurt in case i want to experiment.

    Returns:
        numpy ndarray: Returns an array of intensity integer values with
                       shape=resolution.shape.

    """
    # Initiallising an array of zeros for storing image values.
    image = np.zeros(resolution)
    # Initializing arrays with real and imaginary parts of all the complex
    # values to use in mandelbrot sequence.
    realNums = np.linspace(realMin, realMax, resolution[0])
    imagNums = np.linspace(imagMin, imagMax, resolution[1])

    # Iterating over pixels in picture.
    for z2 in range(resolution[0]):
        for z1 in range(resolution[1]):
            # Gets the corresponding complex number for the current pixel.
            z = complex(realNums[z1], imagNums[z2])
            # Sets x to its initial value to start a new sequence.
            x = x_0

            for i in range(iterations):
                # Checks if the value of the current element in the sequence is
                # larger than two, because if it is, we know that the sequence
                # diverges to infinity.
                if abs(x) >= 2:
                    # Gives the pixel an value with intensity corresponding
                    # to how fast it diverges, then breaks the loop.
                    image[z2, z1] = i
                    break
                else:
                    # Sets x to the next value in the sequence
                    x = x**2 + z
    return(image)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import time
    realMin = -1.5
    realMax = 0.5
    imagMin = -1
    imagMax = 1
    t1 = time.time()
    image = calculate(realMin, realMax, imagMin, imagMax, (1000, 1000), 1000)
    print(time.time() - t1)
    plt.imshow(image, extent=(realMin, realMax, imagMin, imagMax))
    plt.show()
