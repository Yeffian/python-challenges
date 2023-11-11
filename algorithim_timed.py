import datetime


def timed_proc():
    phrase = input('Enter the phrase the lazy fox jumped over the brown dog: ')
    return phrase

start_time = datetime.datetime.now()  # Starts the timer, by putting the time into start_time variable
timed_proc()  # Whatever you want to time
time_taken = datetime.datetime.now() - start_time  # Current time - start time
print(time_taken)  # Printing the time it took