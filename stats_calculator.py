# Calculator For All Static Tests
import math, statistics as stats

options = ["mean", "median", "mode", "min", "max", "range"]

while True:
    print(f"Options: {options}")
    solving = input("What do you want to solve? ")
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



    else:
        print("Pick one from the options above\n")
