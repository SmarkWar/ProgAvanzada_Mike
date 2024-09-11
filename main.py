from coche import Coche

año_actual = 2024

coche1 = Coche("Toyota", "Corolla", 2010)
coche1.mostrar_info()
print(f"Edad del coche1: {coche1.calcular_edad_coche(año_actual)} años")

print("---------------------------------------------")

coche2 = Coche("Ford", "Mustang", 2018)
coche2.mostrar_info()
print(f"Edad del coche2: {coche2.calcular_edad_coche(año_actual)} años")

print("---------------------------------------------")

coche3 = Coche("Tesla", "Model S", 2022)
coche3.mostrar_info()
print(f"Edad del coche3: {coche3.calcular_edad_coche(año_actual)} años")
