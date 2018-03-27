def celsius_to_f(deg_c):
    if deg_c < -273.15:
        return "You are at absolute zero"
    else:
        deg_f = deg_c * (9/5) + 32
        return deg_f

print(celsius_to_f(-300))