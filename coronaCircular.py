print("Corona Circular")
print("")

radio_ma = float(input("Ingresa radio mayor: "))
radio_me = float(input("Ingresa radio menor: "))

area = 3.14 * (radio_ma ** 2 - radio_me ** 2)

perimetro = 2 * 3.14 * (radio_ma + radio_me)

print("")
print("Resultados")
print("==========")
print("Área: ", area.__round__(2))
print("Perímetro: ", perimetro.__round__(2))
