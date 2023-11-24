with open("counter.txt","w") as new_file:
    for i in range(1, 11):
        new_file.write(str(i) + '\n')