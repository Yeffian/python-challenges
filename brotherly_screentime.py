total = int(input('How long can both brothers play for combined? (in minutes)'))
total_secs = total * 60

print('Each brother can play for', total_secs // 2, 'seconds')