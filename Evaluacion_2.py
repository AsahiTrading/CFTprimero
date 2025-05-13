# 2.	Informe el promedio de notas de los varones del listado.
# 3.	Informe cuantos estudiantes sacaron sobre 5.5 en nota de enseñanza media
# 4.	Informe cual fue la nota más baja.
# 5.	En relación al listado de los 500 estudiantes ingresados, indique en qué posición o número de registro se encuentra la nota más alta
# 6.	Documente como resuelve las situaciones pedidas con anterioridad dentro de su código.

### Determinar total de estudiantes 
total_estudiantes = 500
### ¿Cuántos son varones, cuántos mujeres?
varones = int(input("¿Cuántos varones son?: "))
mujeres = total_estudiantes - varones
print(f"Son {mujeres} mujeres")
### Notas de Enseñanza Media según sexo
while True:
    print("\n1.Mujer\n2.Hombre")
    opcion = input("Elige opción: ")
    if opcion == "1":
        cont += 1
        print(f"Notas de Enseñanza media {promedio_mujeres}")
        for i in range (1,500):
            print(f"{mujeres} son mujeres")
    elif opcion == "2":
        varones = int(input(f"Ingrese Nota de Enseñanza Media: "))
        print(f"Notas de enseñanza media {promedio_varones}")
        break
    else:
        print("Opcion inválida")

    
print(f"El promedio de notas de varones es {promedio_varones}")
promedio_varones = notas / varones
notas = float(input("Ingrese su nem: "))
# while total_estudiantes <= 500:
#         contador += 1

# minimo.min(total_estudiantes)
# print(f"La nota más baja fue: {minimo}")
# maximo.max(total_estudiantes)
# print(f"La nota más alta está en el {maximo} lugar")




# print(f"Sacaron nota sobre 5.5 en enseñanza media {nem} estudiantes")