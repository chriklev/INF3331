import numpy as np


def calculate(realMin, realMax, imagMin, imagMax,
              resolution, iterations, x_0=0):
    """Computes an array of intensity values for a given rectangle and
    resolution in the mandelbrot set using numpy vectorization for efficiency.

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
    image = np.zeros(resolution)

    realNums = np.linspace(realMin, realMax, resolution[0])
    imagNums = np.linspace(imagMin, imagMax, resolution[1])
    z = np.sum(np.meshgrid(realNums, imagNums * 1j), axis=0)

    w = np.zeros(resolution, dtype="complex64")

    for i in range(iterations):
        ind = np.less(w, 2)
        image[ind] = i
        w[ind] = w[ind]**2 + z[ind]
    image[image == iterations-1] = 0
    return image


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import time
    realMin = -3.5
    realMax = 0.5
    imagMin = -1
    imagMax = 1
    t1 = time.time()
    image = calculate(realMin, realMax, imagMin, imagMax, (1000, 1000), 1000)
    print(time.time()-t1)
    plt.imshow(image, extent=(realMin, realMax, imagMin, imagMax))
    plt.show()
