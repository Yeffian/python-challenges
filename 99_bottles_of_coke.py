for i in range(99, -1, -1):
    if i == 0:
        break

    bottle = 'bottle' if i == 1 else 'bottles'
    print(f'{i} {bottle} of cola on the wall.', end=' ')
    print(f'{i} {bottle} of cola on the wall, take one down, pass it aroud.')