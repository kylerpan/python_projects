# Calculator For All Static Tests
import math, statistics as stats, numpy as np
from scipy.stats import norm

options = ["mean", "median", "mode", "min", "max", "range", "variance", "standard deviation", "r", "normcdf", "normpdf", "invnorm"]
# options = ["basics", "graph coordinates", "probability"]
# basics = ["mean", "median", "mode", "min", "max", "range", "variance", "standard deviation"]
# graph_coordinates = ["r"]
# probability = ["normcdf", "normpdf", "invnorm"]


def infinity_check (string):
    if string == "+inf":
        return math.inf
    elif string == "-inf":
        return -math.inf
    else:
        return int(string)

while True:
    print(f"Options: {options}")
    solving = input("What do you want to solve? ")

    # || Basics
    if options.index(solving) < 8:
        array = list(map(int, input("What is the list? (enter with one space in between)\n").split(" ")))

        if solving == "mean":
            print(f"The mean of that list is {stats.mean(array)}\n")

        elif solving == "median":
            print(f"The median of that list is {stats.median(array)}\n")
        
        elif solving == "mode":
            print(f"The mode of that list is {stats.mode(array)}\n")

        elif solving == "min":
            print(f"The min of that list is {min(array)}\n")

        elif solving == "max":
            print(f"The max of that list is {max(array)}\n")

        elif solving == "range":
            print(f"The range of that list is {max(array) - min(array)}\n")

        elif solving == "variance":
            print(f"The variance of that list is {stats.variance(array)}\n")

        elif solving == "standard deviation":
            print(f"The standard deviation of that list is {stats.stdev(array)}\n")

    # || For Graph Coordinates
    if options.index(solving) < 9:
        x = list(map(int, input("What are the x coordinates? (enter with one space in between)\n").split(" ")))
        y = list(map(int, input("What are the y coordinates? (enter with one space in between)\n").split(" ")))

        if solving == "r":
            r = np.corrcoef(x, y)[0, 1]
            if r >= 0.8:
                print(f"The correlation coefficient of that data set is strong, r = {np.corrcoef(x, y)[0, 1]}\n")
            elif r >= 0.5:
                print(f"The correlation coefficient of that data set is moderate, r = {np.corrcoef(x, y)[0, 1]}\n")
            else:
                print(f"The correlation coefficient of that data set is weak, r = {np.corrcoef(x, y)[0, 1]}\n")

    # || Probability
    if options.index(solving) < 12:

        if solving == "normcdf":
            lower = infinity_check(input("What is the lower bound? (+inf for positive infinity, -inf for negative infinity) "))
            upper = infinity_check(input("What is the upper bound? (+inf for positive infinity, -inf for negative infinity) "))
            print(f"The probability of data in between those bounds is {norm.cdf(upper) - norm.cdf(lower)}\n")

        if solving == "normpdf":
            variable = infinity_check(input("What is the variable? (+inf for positive infinity, -inf for negative infinity) "))
            print(f"The probability of that variable is {1 - norm.cdf(variable)}\n")

        if solving == "invnorm":
            region = float(input("What is the probabilty region? (+inf for positive infinity, -inf for negative infinity) "))
            print(f"The x value of that region is {norm.ppf(region)}\n")





    else:
        print("Pick one from the options above\n")
