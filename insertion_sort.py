def insertion_sort(n):
    for i in range(1, len(n)):
        key = n[i]
        j = i - 1
        while j >= 0 and key < n[j]:
            n[j + 1] = n[j]
            j -= 1

        n[j + 1] = key


test = [12, 11, 14, 13, 7, 5, 1, 20, 19]
insertion_sort(test)
print(test)