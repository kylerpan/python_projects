# Calculator For All Static Tests
import math, statistics as stats, numpy as np
from scipy.stats import norm
from itertools import permutations, combinations

menu = ["basics", "graph coordinates", "probability", "statistics"]
basics = ["mean", "median", "mode", "min", "max", "range", "variance", "standard deviation"]
graph_coordinates = ["r"]
probability = ["permutations", "combinations", "normcdf", "normpdf", "invnorm"]
statistics = ["one var stats", "two var stats"]

# || Functions
def infinity_check (string):
    if string == "+inf":
        return math.inf
    elif string == "-inf":
        return -math.inf
    else:
        return int(string)

while True:
    print(f"\nMenu: {menu}")
    option = input("What category are you solving? ")

    # || Basics
    if option == "basics":
        print(f"Options: {basics}")
        solving = input("What do you want to solve? (type 'back' to go back) ")

        if solving == "back":
            continue

        if solving not in basics:
            print("Pick one from the options above")
            continue

        # || Conditions
        array = list(map(int, input("What is the list? (enter with one space in between)\n").split(" ")))
        if solving == "mean":
            print(f"The mean of that list is {stats.mean(array)}")

        elif solving == "median":
            print(f"The median of that list is {stats.median(array)}")
        
        elif solving == "mode":
            print(f"The mode of that list is {stats.mode(array)}")

        elif solving == "min":
            print(f"The min of that list is {min(array)}")

        elif solving == "max":
            print(f"The max of that list is {max(array)}")

        elif solving == "range":
            print(f"The range of that list is {max(array) - min(array)}")

        elif solving == "variance":
            print(f"The variance of that list is {stats.variance(array)}")

        elif solving == "standard deviation":
            print(f"The standard deviation of that list is {stats.stdev(array)}")


    # || For Graph Coordinates
    elif option == "graph coordinates":
        print(f"Options: {graph_coordinates}")
        solving = input("What do you want to solve?  (type 'back' to go back) ")

        if solving == "back":
            continue

        if solving not in graph_coordinates:
            print("Pick one from the options above")
            continue

        # || Conditions
        x = list(map(int, input("What are the x coordinates? (enter with one space in between)\n").split(" ")))
        y = list(map(int, input("What are the y coordinates? (enter with one space in between)\n").split(" ")))
        if solving == "r":
            r = np.corrcoef(x, y)[0, 1]
            if r >= 0.8:
                print(f"The correlation coefficient of that data set is strong, r = {np.corrcoef(x, y)[0, 1]}")
            elif r >= 0.5:
                print(f"The correlation coefficient of that data set is moderate, r = {np.corrcoef(x, y)[0, 1]}")
            else:
                print(f"The correlation coefficient of that data set is weak, r = {np.corrcoef(x, y)[0, 1]}")
        

    # || Probability
    elif option == "probability":
        print(f"Options: {probability}")
        solving = input("What do you want to solve?  (type 'back' to go back) ")

        if solving == "back":
            continue

        if solving not in probability:
            print("Pick one from the options above")
            continue

        # || Conditions
        if solving == "permutations":
            array = list(input("What is the list you want the permutations of? (enter with one space in between) ").split(" "))
            perm = permutations(array)
            print("The permutations of that list is:")
            for i in perm:
                print(i)

        if solving == "combinations":
            array = list(input("What is the list you want the combinations of? (enter with one space in between) ").split(" "))
            length = int(input("What is the length that you want the list to be? "))
            comb = combinations(array, length)
            print("The combinations of that list is:")
            for i in comb:
                print(i)

        if solving == "normcdf":
            lower = infinity_check(input("What is the lower bound? (+inf for positive infinity, -inf for negative infinity) "))
            upper = infinity_check(input("What is the upper bound? (+inf for positive infinity, -inf for negative infinity) "))
            print(f"The probability of data in between those bounds is {norm.cdf(upper) - norm.cdf(lower)}")

        elif solving == "normpdf":
            variable = infinity_check(input("What is the variable? (+inf for positive infinity, -inf for negative infinity) "))
            print(f"The probability of that variable is {1 - norm.cdf(variable)}")

        elif solving == "invnorm":
            region = float(input("What is the probabilty region? (+inf for positive infinity, -inf for negative infinity) "))
            print(f"The x value of that region is {norm.ppf(region)}")

    # || Statistics
    elif option == "statistics":
        print(f"Options: {statistics}")
        solving = input("What do you want to solve?  (type 'back' to go back) ")

        if solving == "back":
            continue

        if solving not in statistics:
            print("Pick one from the options above")
            continue

        # || Conditions
        if solving == "one var stats":
            array = list(map(int, input("What is the list? (enter with one space in between)\n").split(" ")))
            c1 = ["Mean", "Summation", "Standard deviation", "Length", "Min", "Q1", "Median", "Q3", "Max"]
            c2 = [stats.mean(array), sum(array), stats.stdev(array), len(array), min(array), 
                    np.percentile(array, 25), stats.median(array), np.percentile(array, 75), max(array)]

            for i in range(9):
                row = "{:19} {:f}".format(c1[i], c2[i])
                print(row)



    else:
        print("Pick one from the options above")
