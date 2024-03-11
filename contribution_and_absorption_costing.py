def absorption_cost(labor, material, manufacturing_variable, manufacturing_fixed, units):
    return (labor + material + manufacturing_variable + manufacturing_fixed) / units

def contribution_cost(rev, costs):
    return (rev - costs) / rev
