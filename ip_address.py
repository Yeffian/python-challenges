import ipaddress
import random

def random_ipv6(n):
    addresses = []

    for i in range(n):
        address = ipaddress.IPv6Address._string_from_ip_int(
            random.randint(0, ipaddress.IPv6Address._ALL_ONES)
        )

        addresses.append(address)
    
    return addresses

print(random_ipv6(100))

