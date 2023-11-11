def calculate_check_digit(isbn_n):
    isbn_number = str(isbn_n)[0:12]
    one_or_three = True
    isbn_sums = []

    for number in isbn_number:
        mul_digit = 1 if one_or_three is True else 3
        isbn_sums.append(int(number) * mul_digit)
        one_or_three = not one_or_three
    
    modded_sum = sum(isbn_sums) % 10
    if modded_sum == 0:
        return 0
    else:
        return 10 - modded_sum
    

print(calculate_check_digit(9781681972712))
    