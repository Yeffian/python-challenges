def bmi(w, h):
    index = w / h ** 2

    if index < 18.5:
        return "Underweight"
    if 18.5 <= index:
        return "Normal weight"
    if 25.0 <= index < 30.0:
        return "Overweight"
    if 30.0 <= index:
        return "Obseity"


weight = input('Enter your weight (Kg): ')
height = input('Enter your height: (meters): ')

print(bmi(float(weight), float(height)))