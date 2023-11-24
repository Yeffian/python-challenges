from datetime import datetime

def twelve_to_twenty_four(time):
    time = datetime.strptime(time, '%I:%M %p')
    return time.strftime('%H:%M:%S')


print(twelve_to_twenty_four('6:30 PM'))