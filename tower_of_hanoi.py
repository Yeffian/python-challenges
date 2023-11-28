def tower_of_hanoi(n, rod_A, rod_C, rod_B):
    actions = []
    if n == 1:
        actions.append(f"Disk 1 = {rod_A} -> {rod_C}")
        return
    tower_of_hanoi(n - 1, rod_A, rod_B, rod_C)
    actions.append(f"Disk {n} = {rod_A} -> {rod_C}")
    tower_of_hanoi(n - 1, rod_B, rod_C, rod_A)
    return actions