# taking a two sample z test
import math

def get_mean(array):
    sum = 0
    for value in array:
        sum += value
    mean = sum/len(array)
    return mean

def get_sd(array, mean):
    numerator = 0
    for value in array:
        numerator += (value - mean) ** 2
    sd = math.sqrt(numerator / (len(array) - 1))
    return sd

# sample values
sample_one = list(map(int, input("\nWhat are the values for the first sample? (enter with one space in between)\n").split(" ")))
sample_two = list(map(int, input("\nWhat are the values for the second sample? (enter with one space in between)\n").split(" ")))
print(f"\nSample One: {sample_one}")
print(f"Sample Two: {sample_two}")

# means
sample_one_mean = get_mean(sample_one)
sample_two_mean = get_mean(sample_two)
print(f"\nSample One Mean: {sample_one_mean}")
print(f"Sample Two Mean: {sample_two_mean}")

# standard deviations
sample_one_sd = get_sd(sample_one, sample_one_mean)
sample_two_sd = get_sd(sample_two, sample_two_mean)
print(f"\nSample One Standard Deviation: {sample_one_sd}")
print(f"Sample Two Standard Deviation: {sample_two_sd}")

# two sample z test
mean_diff = sample_one_mean - sample_two_mean
denominator = math.sqrt((sample_one_sd ** 2)/len(sample_one) + (sample_two_sd ** 2)/len(sample_two))
z_score = mean_diff / denominator
print(f"\nZ score: {z_score}")

# significance
if abs(z_score) >= 1.64485362591:
    print("\nThere IS a signifant difference at a 0.05 signficance level.\n")
else: 
    print("\nThere ISN'T a signifant difference at a 0.05 signficance level.\n")