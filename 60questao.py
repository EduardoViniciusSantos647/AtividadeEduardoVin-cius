def fahrenheit_para_celsius(f):
    c = (5 / 9) * (f - 32)
    return c




temperatura_f = float(input("Digite a temperatura em Fahrenheit: "))


temperatura_c = fahrenheit_para_celsius(temperatura_f)

print(temperatura_f, "F equivale a", temperatura_c, "C")