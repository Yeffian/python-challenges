bus_time = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]
bus_capacity = [40, 40, 40, 40, 40, 40, 40, 64]
bus_money = [0, 0, 0, 0, 0, 0, 0, 0]
charge=15

bus_choice = int(input("\nChoose your Bus. Please enter 09:00 [0], 11:00 [2],13:00 [4] or 15:00 [6]: "))
print("Bus time chosen:",bus_time[bus_choice])

if bus_choice not in [0, 2, 4, 6]:
    print("Not a valid bus to KL City Centre.")

bus_capacity[bus_choice]= bus_capacity[bus_choice] - 1
bus_money[bus_choice] += charge

print("\nUpdated Lists")
print("Bus Times",bus_time)
print("Bus capacity", bus_capacity)
print("Bus money", bus_money)

return_bus_choice = int(input("\nChose your return bus. Please enter 09:00 [0], 11:00 [2],13:00 [4] or 15:00 [6]: "))
print("Chosen Return Bus Time: ", bus_time[return_bus_choice])

if return_bus_choice not in [0, 2, 4, 6]:
    print("Not a valid bus to KL City Centre.")

bus_capacity[return_bus_choice]= bus_capacity[bus_choice] - 1
bus_money[bus_choice] += charge

print("\nUpdated Lists")
print("Bus Times",bus_time)
print("Bus capacity", bus_capacity)
print("Bus money", bus_money)
