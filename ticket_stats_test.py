# two sample z test
# determines if randomly picking numbers with checking recurrence 
# is better than not checking

from random import choice
import math, time

start_time = time.time()  #gets the start time
random_list = [1, 2, 3, 4, 5] 
sample = 30

""" How to get a new ticket """
def new_ticket():
    ticket = []

    while len(ticket) < 4:  #checks to see if 4 or less characters
        choosen_one = choice(random_list)  #chooses randomly form random_list
        copy = False

        for character in ticket:
            if choosen_one == character:  #checks if there is a repeat of characters
                copy = True
        
        if copy == False:
            ticket.append(choosen_one)  #adds character into the ticket

    return ticket

""" How to find the mean """
def get_mean(times):
    sum = 0
    length = len(times) 
    for time in times:  #sums up all the trials
        sum += time
    mean = sum/length
    return mean

""" How to find the standard deviation """
def get_sd(times, mean):
    numerator = 0
    for time in times:  #sums up all the trials
        numerator = (time - mean) ** 2
    sd = math.sqrt(numerator / (sample - 1))
    return sd

""" How to find 2 sample z test """
def get_two_sample_z_test(mean1, sd1, mean2, sd2):
    mean_diff = mean1 - mean2
    denominator = math.sqrt(((sd1) ** 2 + (sd2) ** 2) / sample)
    z = mean_diff / denominator
    return z

""" How to find significance """
def get_sig(z):
    if abs(z) >= 1.64485362591:
        print("There IS a signifant difference at a 0.05 signficance level.")
    else: 
        print("There ISN'T a signifant difference at a 0.05 signficance level.")


""" How the raffle ticket is picked """
ticket = []
ticket = new_ticket()


""" My ticket with checking if recurring """
my_ticket_wcheck = []
my_ticket_wcheck = new_ticket()
times_wcheck = []
counter_wcheck = 0
tried = []

for n in range(sample):
    while True:  #while the ticket doens't match
        if my_ticket_wcheck == ticket:
            # print(counter_wcheck)
            my_ticket_wcheck = new_ticket()  #creates a new ticket 
            times_wcheck.append(counter_wcheck)  #adds the counter to the list
            counter_wcheck = 0  #resets the counter 
            tried = []  #resets the tried list 
            break
        else: 
            tried.append(my_ticket_wcheck)  #adds ticket to tired list
            # print(my_ticket_wcheck)
            my_ticket_wcheck = new_ticket()  #creates a new ticket
            count = 0  
            while count == 0:  #0 equals when ticket matches tried list
                for tries in tried:  #for the tickets in tried
                    if my_ticket_wcheck == tries:
                        my_ticket_wcheck = new_ticket()  #creates a new ticket because of match
                        count = 0  #sets count to 0 b/c match
                        break
                    else:
                        count = 1  #sets ocunt to 1 b/c no match
            counter_wcheck += 1  #adds to the times tried 


""" My ticket with out checking if recurring """
my_ticket_wocheck = []
my_ticket_wocheck = new_ticket()
times_wocheck = []
counter_wocheck = 0

for n in range(sample):
    while True:
        if my_ticket_wocheck == ticket:
            # print(counter_wocheck)
            my_ticket_wocheck = new_ticket()
            times_wocheck.append(counter_wocheck) 
            counter_wocheck = 0
            break
        else: 
            # print(my_ticket_w0check)
            my_ticket_wocheck = new_ticket()
            counter_wocheck += 1


#getting the ticket number
print("The lucky winner is:")
for character in ticket:
    print(character, end = "")  #prints without new line
print("")

#getting the mean and sd of w check
print("\nMy ticket with checking if recurring:")
times_wcheck_mean = get_mean(times_wcheck)
print(f"Mean = {times_wcheck_mean}")
times_wcheck_sd = get_sd(times_wcheck, times_wcheck_mean)
print(f"Standard Deviation = {times_wcheck_sd}")

#getting the mean and sd of w/o check
print("\nMy ticket with out checking if recurring:")
times_wocheck_mean = get_mean(times_wocheck)
print(f"Mean = {times_wocheck_mean}")
times_wocheck_sd = get_sd(times_wocheck, times_wocheck_mean)
print(f"Standard Deviation = {times_wocheck_sd}")

#getting the z score
print("\n2 sample z score:")
z_score = get_two_sample_z_test(times_wcheck_mean, times_wcheck_sd, times_wocheck_mean, times_wocheck_sd)
print(f"z = {z_score}\n")

#seeing significance
get_sig(z_score)

time = time.time() - start_time
print(f"\n--- {time} seconds ---")

