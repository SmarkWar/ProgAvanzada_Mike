try:
    numero1 = 10
    numero2 = 0
    
    division = numero1/numero2
    
    print(numero2)
    
except ZeroDivisionError as e:
    print(f"Estas tratando de dividir entre 0.{e}")
    