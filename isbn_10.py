def calculate_check_digit(isbn_n):
    isbn_sums = []
    mul_nums = [10, 9, 8, 7, 6, 5, 4, 3, 2]

    for i in range(len(str(isbn_n)) - 1):
        # print(int(str(isbn_n)[i]) * mul_nums[i])
        isbn_sums.append(int(str(isbn_n)[i]) * mul_nums[i])
    
    modded_sum = sum(isbn_sums) % 11
    
    return 11 - modded_sum
    

print(calculate_check_digit(1841462012))
    