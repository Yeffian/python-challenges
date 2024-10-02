suvat = ['s', 'u', 'v', 'a', 't', 'v^2']


def ask_for(part):
    x = ''
    if part == 's':
        x = float(input('Please enter the displacement (m): '))
    elif part == 'u':
        x = float(input('Please enter the initial velocity (m/s): '))
    elif part == 'v':
        x = float(input('Please enter the final velocity (m/s): '))
    elif part == 'a':
        x = float(input('Please enter the acceleration (m/s^2): '))
    elif part == 't':
        x = float(input('Please enter the time (s): '))
    return x


def find(variable):
    if variable == 'v':
        u = ask_for('u')
        a = ask_for('a')
        t = ask_for('t')

        return u + a * t
    if variable == 'v^2':
        u = ask_for('u')
        a = ask_for('a')
        s = ask_for('s')

        return u ** 2 + 2 * a * s
    elif variable == 's':
        option = input('Would you like to use initial velocity (u), final velocity (v) or both? (a) ')
        if option == 'u':
            u = ask_for('u')
            a = ask_for('a')
            t = ask_for('t')

            return u * t + 1 / 2 * a * t ** 2
        elif option == 'v':
            v = ask_for('v')
            a = ask_for('a')
            t = ask_for('t')

            return v * t + 1 / 2 * a * t ** 2
        elif option == 'a':
            u = ask_for('u')
            v = ask_for('v')
            t = ask_for('t')

            return 1 / 2 * (v + u) * t


unknown = input('What are you trying to find? ').lower()

if unknown not in suvat:
    print('That variable does not exist in the SUVAT equations of motion.')

print(find(unknown))