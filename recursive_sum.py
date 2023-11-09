def sum_recursive(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_recursive(number // 10)

print(sum_recursive(45))