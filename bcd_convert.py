def dernary_to_bcd(n): 
    rev = 0
 
    while n > 0: 
        rev = rev * 10 + (n % 10)
        n = n // 10
 
    while (rev > 0) : 
        b = str(rev % 10)
        print("{0:04b}".format(int(b, 16)), end = " ") 
        rev = int(rev / 10)

dernary = input('Enter your denary number: ')
print(int(dernary) + ' in BCD is ' + dernary_to_bcd(int(dernary_to_bcd)))