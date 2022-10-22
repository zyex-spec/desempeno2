mayor = lambda numero1, numero2: 1 if numero1>numero2 else -1

MostrarMayor = lambda numero: "el primer numero es menor" if numero == 1 else "el segundo numero es mayor"
print(MostrarMayor(mayor(20,23)))