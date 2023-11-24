from time import strftime, gmtime

starting_hour = 2
charge_time = 51

end_time = (2 * 3600) + (51 * 3600)

print(strftime('%H:%M:%S', gmtime(end_time)))