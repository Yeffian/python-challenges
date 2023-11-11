def decimal_to_roman(num):
    result = ""
    if num >= 1000:
        result += "M"
        result += decimal_to_roman(num - 1000)
    elif num >= 900:
        result += "CM"
        result += decimal_to_roman(num - 900)
    elif num >= 500:
        result += "D"
        result += decimal_to_roman(num - 500)
    elif num >= 400:
        result += "CD"
        result += decimal_to_roman(num - 400)
    elif num >= 100:
        result += "C"
        result += decimal_to_roman(num - 100)
    elif num >= 90:
        result += "XC"
        result += decimal_to_roman(num - 90)
    elif num >= 50:
        result += "L"
        result += decimal_to_roman(num - 50)
    elif num >= 40:
        result += "XL"
        result += decimal_to_roman(num - 40)
    elif num >= 10:
        result += "X"
        result += decimal_to_roman(num - 10)
    elif num >= 9:
        result += "IX"
        result += decimal_to_roman(num - 9)
    elif num >= 5:
        result += "V"
        result += decimal_to_roman(num - 5)
    elif num >= 4:
        result += "IV"
        result += decimal_to_roman(num - 4)
    elif num >= 1:
        result += "I"
        result += decimal_to_roman(num - 1)
    
    return result

for i in range(1, 100):
    print(decimal_to_roman(i))