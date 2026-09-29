def inverter_texto(texto):
    invertido = ""

    for letra in texto:
        invertido = letra + invertido

    return invertido


print(inverter_texto("python2023"))
print(inverter_texto("0203programacao2023"))
print(inverter_texto("luz azul"))
print(inverter_texto("arara rara"))
print(inverter_texto("anotaram a data da maratona"))