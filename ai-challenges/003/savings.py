acumulado = 0
meta = int(input("Dime cual tu meta de ahorro: "))

while acumulado <= meta:
    cantidadIngresada = int (input ("Cuanto deseas ingresar?: "))
    acumulado = cantidadIngresada + acumulado
    print(f"La cantidad ahorrada es: {acumulado} ")
    if acumulado < meta:
        restante = meta - acumulado
        print (f"Te falta: {restante}") 
print ("MUY BIENNN, LO LOGRASTEEEEE")