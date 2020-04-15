# Data Structures and Algorithms in Python Ch.1 (Goodrich et. al.)
# Project exercise P1.35
# Ryoh Shinohara
# =======================================================================================
# The birthday paradox says that the probability that two people in a room will have the
# same birthday is more than half, provided n, the number of people in the room, is more
# than 23. This property is not really a paradox, but many people find it surprising.
# Design a Python program that can test this paradox by a series of experiments on
# randomly generated birthdays, which test this paradox for n = 5,10,15,20,...,100.

from random import randrange

daysInYear = 365
experiments = 1000

def generateBirthdays(numDays):
    """
    Generates numDays number of random integers that correspond to days of
    the year. February 29th will be considered day 366 for convenience.
    """
    birthdays = []
    for i in range(numDays):
        isLeapYear = randrange(numDays) == 0
        if isLeapYear:
            birthdays.append(randrange(daysInYear + 1))
        else:
            birthdays.append(randrange(daysInYear))
    return birthdays

def hasSameBirthday(birthday):
    """
    Given a list of birthdays, returns boolean for whether there are same
    birthdays
    """
    return len(birthday) != len(set(birthday))

def paradoxExperiment(numDays, numExperiments):
    """
    Generates numExperiments number of trials with numDays number of
    birthdays and yields the proportion of trials that contained duplicate
    birthdays
    """
    experiments = [hasSameBirthday(generateBirthdays(numDays)) for i in range(numExperiments)]
    countTrue = sum(1 for i in experiments if i)
    return countTrue / numExperiments

def main():
    print("Generating birthday paradox experiments with {} trials per experiment...".format(experiments))
    for i in range(5, 101, 5):
        print("{} people per room: {}".format(i, paradoxExperiment(i, experiments)))

if __name__ == "__main__":
    main()