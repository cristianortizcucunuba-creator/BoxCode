dias = [
"ingrese temperatura del lunes: ",
"ingrese temperatura del martes: ",
"ingrese temperatura del miercoles: ",
"ingrese temperatura del jueves: ",
"ingrese temperatura del viernes: ",
"ingrese temperatura del sabado: ",
"ingrese temperatura del domingo: "
]


tempSemana = []

for i in range(7):
    temps = int (input(dias[i]))
    tempSemana.append(temps)
print(tempSemana)