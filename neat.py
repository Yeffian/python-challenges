def sum_recursive(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_recursive(number // 10)

def neat_nums(start, end):
    result = []

    for i in range(start, end + 1):
        s = sum_recursive(i)
        if i % s == 0:
            result.append(i)
    
    return result


print(neat_nums(101, 1000))