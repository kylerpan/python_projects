# area of circle = pi*r^2
# area of square = s^2

# random(0, 1)
# {for loop (sample = 100)
# random x, y 
# counter = 0
# x^2 + y^2 = 1 
# if <= 1, counter ++}
# print(4 * counter / 100)

import random as r

def pi(sample):

    counter = 0  #number of points in circle
    for number in range(sample):
        x = r.uniform(0, 1) 
        y = r.uniform(0, 1)  #makes x, y points

        value = x ** 2 + y ** 2

        if (value <= 1):  #checks to see if in circle
            counter += 1 
        
    pi = 4 * counter / sample  #equation to get pi
    print(pi)

def kyle_main():  #my way of solving
    number = 10
    while number <= 100000:
        pi(number)
        number = number * 10

def bryan_main():  #bryan's way of solving
    array = [10, 100, 1000, 10000, 100000, 1000000]
    for index, item in enumerate(array):  #enumerate gets both index and value
        print(f"Current i: {index} | Current item: {item}")
        pi(item)

if __name__ == "__main__":  #only runs things in pi.py
    kyle_main()
