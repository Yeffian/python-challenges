limit = int(input('What is your limit? '))
table_num = int(input('What will the table number be? '))

for i in range(limit):
    print(f'{i + 1} + {table_num} = {(i + 1) + table_num}')