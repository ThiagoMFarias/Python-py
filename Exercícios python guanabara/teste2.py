temperature = 50

if temperature < 0:
    print("Está muito frio lá fora!")
elif temperature >= 0 and temperature < 10:
    print("Está frio lá fora.")
elif temperature >= 10 and temperature < 20:
    print("Está fresco lá fora.")
elif temperature >= 20 and temperature < 30:
    print("Está agradável lá fora.")
else:
    print("Está quente lá fora!")
