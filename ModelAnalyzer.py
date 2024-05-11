#!/usr/bin/env python
import numpy as np
from scipy.optimize import curve_fit
import csv
import matplotlib.pyplot as plt

class ModelAnalyzer():
    """
    A class for analyzing models, including functions for calculating exhaust velocity,
    generating exponentially distributed data points, and plotting graphs.

    Attributes:
        None
    """

    @staticmethod
    def exp_func(x, a, b):
        return a * np.exp(b * x)

    @staticmethod
    def Ve_caculation(csv_read_file: str) -> tuple[tuple[list[float], list[float]], tuple[float, float]]:
        """
        Calculate Ve (volumetric efficiency) with respect to Watts based on data from a CSV file.

        Parameters:
            csv_read_file (str): The file path to the CSV file containing the data.

        Returns:
            tuple: A tuple containing two tuples:
                1. Tuple of original data (x, y).
                2. Tuple of fitted parameters (a, b).

        CSV Format:
            The CSV file is expected to have two columns:
            - Column 1: Independent variable (typically Watts).
            - Column 2: Dependent variable (typically Ve).

        This function reads data from a CSV file specified by 'csv_read_file'.
        It then fits an exponential function to the data using curve fitting.
        The fitted parameters 'a' and 'b' are calculated and returned in a tuple.
        Additionally, the original data and the fitted parameters are returned in separate tuples
        within the main tuple, providing insight into both the raw data and the fitted model.

        Fitted Function: a*e^(x*b)
        """

        x = []
        y = []
        with open(csv_read_file, "r") as csvdata:
            csv_reader = csv.reader(csvdata)

            next(csv_reader)
            for row in csv_reader:
                x.append(float(row[0]))
                y.append(float(row[1]))

        popt, pcov = curve_fit(ModelAnalyzer.exp_func, x, y)

        a = popt[0]
        b = popt[1]

        print(f"Function, as Ve relates to Watts:\n{a}*e^(x*{b})")

        return (x, y), (a, b)

    @staticmethod
    def data_gen_exp(exp_function: tuple, write_file: str) -> tuple[tuple[float, float], tuple[list, list]]:
        """
        Generates exponentially distributed data points based on the provided exponential function parameters.

        Parameters:
            exp_function (tuple): A tuple containing the maximum and minimum values (float) and the parameters 'a' and 'b' (float)
                                 for the exponential function (max, min, a, b).
            write_file (str): The file path to write the generated data points in CSV format.

        Returns:
            tuple: A tuple containing four arrays:
                1. Tuple of the original range (min, max).
                2. Tuple of newly generated data points for plotting (x_new, y_new).

        The function generates 'y' data points based on the given exponential function parameters and evenly spaced 'x' values.
        It then writes the generated data to a CSV file specified by 'write_file'. The CSV file contains two columns: 'Ve' and 'Watts'.
        The function returns two tuples: one representing the original range and the other containing the newly generated data points.
        """
        _max = exp_function[0]
        _min = exp_function[1]
        a = exp_function[2]
        b = exp_function[3]

        x_new = np.linspace(_min, _max, 500)  # new data points for plotting
        y_new = a * np.exp(b * x_new)

        with open(write_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Ve", "Watts"])
            for i in range(len(x_new)):
                writer.writerow([round(x_new[i], 2), round(y_new[i], 2)])
        return (_min, _max), (x_new, y_new)

    @staticmethod
    def graph(
        arrays1: tuple,
        arrays2: tuple,
        label1: str = "Label 1",
        label2: str = "Label 2",
        xlabel: str = "X_Axis",
        ylabel: str = "Y_Axis",
    ) -> None:
        """
        Plot two sets of data points using Matplotlib.

        Parameters:
            arrays1 (tuple): A tuple containing two arrays representing the x and y data points for the first dataset.
            arrays2 (tuple): A tuple containing two arrays representing the x and y data points for the second dataset.
            label1 (str, optional): Label for the first dataset (default is "Label 1").
            label2 (str, optional): Label for the second dataset (default is "Label 2").
            xlabel (str, optional): Label for the x-axis (default is "X_Axis").
            ylabel (str, optional): Label for the y-axis (default is "Y_Axis").

        Returns:
            None

        This function plots two sets of data points using Matplotlib. It takes in two tuples,
        each containing two arrays representing the x and y data points for a dataset.
        The function then plots the data points with specified labels on a graph with the provided
        x-axis and y-axis labels. If labels are not defined, default labels are used.
        """
        print(f"Graphing: {xlabel}(x) by {ylabel}(y)")
        plt.plot(arrays1[0], arrays1[1], "o", label=label1)
        plt.plot(arrays2[0], arrays2[1], "-", label=label2)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    analyzer = ModelAnalyzer()

    x_y, components = analyzer.Ve_caculation("Ve_data_new.csv")
    min_max, arrays = analyzer.data_gen_exp(
        (0, 30, components[0], components[1]), "Ve_caculation.csv"
    )
    analyzer.graph(x_y, arrays, "Data", "Curve", "Ve_new", "Watts")

    x_y, components = analyzer.Ve_caculation("Ve_data.csv")
    min_max, arrays = analyzer.data_gen_exp(
        (0, 30, components[0], components[1]), "Ve_caculation.csv"
    )
    analyzer.graph(x_y, arrays, "Data", "Curve", "Ve_old", "Watts")
