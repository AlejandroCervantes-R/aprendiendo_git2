gastos_total = []
while True:
    try:
        gasto = input(f"escribe tus gastos: ")
        if gasto.lower() == "q":
            print("haz salido")
            break
        gasto = int(gasto) 
        gastos_total.append(gasto)
    except ValueError: 
        print("valor no valido")
        continue
total = sum(gastos_total)
cantidad_gastos = len(gastos_total)
promedio = (total / cantidad_gastos)
print(f"este es el total{total:.2f}")
print(f"este es tu promedio {promedio:.2f}")
print(f"esta es tu cantidad de gastos {cantidad_gastos}")