import sys
from mandelbrot_1 import calculate as man1
from mandelbrot_2 import calculate as man2
from mandelbrot_3 import calculate as man3
import matplotlib.pyplot as plt
import time

helpMsg = ("Command line arguments:\n"
           "    --help: Displays this message."
           "    1/2/3: Sets the method of calculation to standard python,"
           "numpy vectorization and jit'ing respectivly."
           "Following commands are allowed:\n"
           "    exit/quit/q: Exits the script.\n"
           "    help: Displays this message.\n"
           "    setScript: Lets you to set witch script to use.\n"
           "    setParams: Lets you set the parameters for a run.\n"
           "    run: Runs the script with current parameters and saves"
           "to file.")


# initializing different default values
funcs = [man1, man2, man3]
quit = 0
script = 3
path = "mandelbrot.png"
realMin = -1.5
realMax = 0.5
imagMin = -1
imagMax = 1
resolution = (1000, 1000)
iterations = 1000

print("Welcome to mandelbrotmanager!\n")

# Checks for command line arguments
if len(sys.argv) > 1:
    if sys.argv[1] == "--help":
        print(helpMsg)
        quit = 1
    elif sys.argv[1] == "1" or sys.argv[1] == "2" or sys.argv[1] == "3":
        script = int(sys.argv[1])

while not quit:
    inp = input(" : ")

    if inp == "exit" or inp == "quit" or inp == "q":
        print("Exiting script")
        quit = 1

    elif inp == "help":
        print(helpMsg)

    elif inp == "setScript":
        print("1 for standard python script\n"
              "2 for numpy-vectorized script\n"
              "3 for jit'et script")
        script = int(input("script nr.: "))

    elif inp == "setParams":
        realMin = float(input("Minimum real value: "))
        realMax = float(input("Maximum real value: "))
        imagMin = float(input("Minimum imaginary value: "))
        imagMax = float(input("Maximum imaginary value: "))
        width = int(input("Width of picture: "))
        height = int(input("Height of picture: "))
        resolution = (width, height)
        iterations = int(input("Iterations in sequence: "))
        path = input("Filepath: ")

    elif inp == "run":
        t1 = time.time()
        plt.imshow(funcs[script - 1](realMin, realMax, imagMin, imagMax,
                                     resolution, iterations),
                   extent=(realMin, realMax, imagMin, imagMax))
        t2 = time.time()
        plt.savefig(path)
        print("Data calculations took %.3f" % (t2 - t1))
        print("Picture saved to path: ", path)

    else:
        print("Thats not an allowed command. Try again.")
