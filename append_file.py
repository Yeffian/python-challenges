with open("counter.txt", "r+") as file:
    numbers = [int(i) for i in file.readlines()]
    print(numbers[-1])  
    for i in range(numbers[-1] + 1  , numbers[-1] + 11):
        file.write(str(i) + '\n')