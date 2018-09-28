from PIL import Image
import numpy as np

realLower = -1.5
realUpper = 0.5
imagLower = -1
imagUpper = 1
resolution = 1000, 1000
image = np.zeros((resolution[0], resolution[1], 3), dtype=np.uint8)
N = 1000

realNums = np.linspace(realLower, realUpper, resolution[0])
imagNums = np.linspace(imagLower, imagUpper, resolution[1])


def f(x, c):
    return(x**2 + c)


for z2 in range(len(imagNums)):
    for z1 in range(len(realNums)):
        z = complex(realNums[z1], imagNums[z2])
        x = 0
        for i in range(N):
            if abs(x) >= 2:
                image[z1, z2] = [i * 255 / N, 0, 0]
                break
            else:
                x = f(x, z)

img = Image.fromarray(image, 'RGB')
img.save("mandelbrot_1.png")
img.show()
print(image[:, :, 0])
