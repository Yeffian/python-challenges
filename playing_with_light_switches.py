def toggled_light_switches(lights, numbers):
    light_buffer = []
    switches = [False for switch in range(lights)]
    for rng in numbers:
        s = min(rng)
        e = max(rng)

        for i in range(s, e + 1):
            switches[i] = not switches[i]

    return switches.count(True)


data = [[616, 293],
[344, 942],
[27, 524],
[716, 291],
[860, 284],
[74, 928],
[970, 594],
[832, 772],
[343, 301],
[194, 882],
[948, 912],
[533, 654],
[242, 792],
[408, 34],
[162, 249],
[852, 693],
[526, 365],
[869, 303],
[7, 992],
[200, 487],
[961, 885],
[678, 828],
[441, 152],
[394, 453]]
print(toggled_light_switches(1000, data))