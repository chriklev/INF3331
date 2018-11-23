import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_temperature(months, time_bounds=None, y_bounds=None):
    """Plots the temperatures of given months vs years

    Args:
        months (string): The month for witch temperature values to plot. Can
            also be list of strings with several month names.
        time_bounds (tuple or list): Optional argument with minimum and maximum
            for the years to plot. Must be tuple or list, of integers or floats
            on the form: (minimum, maximum)
        y_bounds (tuple or list): Optional argument with minimum and maximum
            for the y-axis. Must be tuple or list, of integers or floats
            on the form: (minimum, maximum)

    """
    temperatures = pd.read_csv(
        "temperature.csv",
        usecols=["Year"].append(months))

    if time_bounds:
        bounds = temperatures["Year"].map(
            lambda x: x >= time_bounds[0] and x <= time_bounds[1])
        temperatures = temperatures[bounds]

    temperatures.plot("Year", months, ylim=y_bounds)
    plt.title("Temperature vs. year for given months")
    plt.xlabel("time [years]")
    plt.ylabel("temperature [celsius]")


def plot_CO2(time_bounds=None, y_bounds=None):
    """Plots global carbon emmissions vs years

    Args:
        time_bounds (tuple or list): Optional argument with minimum and maximum
            for the years to plot. Must be tuple or list, of integers or floats
            on the form: (minimum, maximum)
        y_bounds (tuple or list): Optional argument with minimum and maximum
            for the y-axis. Must be tuple or list, of integers or floats
            on the form: (minimum, maximum)

    """
    co2 = pd.read_csv("co2.csv")

    if time_bounds:
        bounds = co2["Year"].map(
            lambda x: x >= time_bounds[0] and x <= time_bounds[1])
        co2 = co2[bounds]

    co2.plot("Year", "Carbon", ylim=y_bounds, legend=False)
    plt.title("Global carbon emmissions vs. year")
    plt.xlabel("time [years]")
    plt.ylabel("carbon emmissions [million metric tons]")


if __name__ == "__main__":
    plot_CO2()
    plt.show()
    plot_temperature(
        ["January", "February", "March"])
    plt.show()
