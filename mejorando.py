### Aislar variables
notas = []; sexos = []; cantidad = 5; mujeres = 0
suma_varones = 0; cont_sobre_5_5 = 0; nota_minima = 8
nota_maxima = 0; posicion_maxima = 0
### Instrucciones al Usuario.
print("Ingrese las notas y el sexo de los estudiantes (h/m):")
# Ingreso de datos
for i in range(cantidad):
    nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
    sexo = input(f"Ingrese el sexo del estudiante {i+1} (h/m): ").lower()
    
    notas.append(nota)
    sexos.append(sexo)

    # Actualizando estadísticas
    if nota > nota_maxima:
        nota_maxima = nota
        posicion_maxima = i + 1
    if nota < nota_minima:
        nota_minima = nota
    if nota > 5.5:
        cont_sobre_5_5 += 1
    if sexo == "m":
        mujeres += 1
    elif sexo == "h":
        suma_varones += nota

# Cálculo del promedio de varones
promedio_varones = suma_varones / (cantidad - mujeres)

# Resultados
print("\nResultados: ")
print(f"1. La cantidad de mujeres es: {mujeres}")
print(f"2. El promedio de notas de los varones es: {promedio_varones}")
print(f"3. {cont_sobre_5_5} estudiantes sacaron sobre 5.5 en notas de enseñanza media.")
print(f"4. La nota más baja fue: {nota_minima}")
print(f"5. La nota más alta está en la posición: {posicion_maxima}")

# Documentación:
# 1. Se cuenta el número de mujeres incrementando un contador cada vez que se encuentra una "m" en la lista de sexos.
# 2. Se calcula el promedio de notas de los varones sumando sus notas y dividiendo por la cantidad de varones.
# 3. Se cuenta cuántos estudiantes tienen notas mayores a 5.5.
# 4. Se encuentra la nota mínima comparando cada nota ingresada.
# 5. Se encuentra la nota máxima y su posición en la lista de notas.
# 6. Se imprime el resultado de cada cálculo al final.
# 7. Se utiliza un bucle for para iterar sobre la cantidad de estudiantes y se ingresan los datos uno por uno.
