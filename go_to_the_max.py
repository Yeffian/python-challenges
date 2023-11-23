nn = int(input('Enter rows: '))
mm = int(input('Enter columns: '))

result = []
dot_or_cross = False

for i in range(nn):
    row = []
    for j in range(mm):
        dot_or_cross = not dot_or_cross
        row.append('.' if dot_or_cross else '*')
    result.append(row)

print(result)