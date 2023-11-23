def binary_search(n, t, r):
    low = 0
    mid = 0
    high = len(n) - 1

    while low <= high:
        mid = (high + low) // 2

        if n[mid] < t:
            low = mid + 1
        elif n[mid] > t:    
            high = mid - 1
        else:
            return mid

    if r == 0:          
        return -1
    else:
        return binary_search(n, t, r-1)


def bulletproof_binary_search(n, t, r):
    return binary_search(n, t, 2)


print(bulletproof_binary_search([2, 3, 4, 10, 40], 10, 2))
