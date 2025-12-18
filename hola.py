gastos_total = []
while True:
    try:
        gasto = int(input(f"escribe tus gastos: "))
        gastos_total.append(gasto)
    except ValueError:
        print("valor no valido")
        continue
