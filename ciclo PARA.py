sumaGlobal = 0
totalAlumnos = 0
print("ingrese numero de salones")
salones = int(input())
for i in range(1, salones + 1, 1):
    sumaNotasSalon = 0
    print("Ingrese  alumnos de este salon")
    alumnos = int(input())
    for j in range(1, alumnos + 1, 1):
        print("ingrese nota del estudiante")
        nota = float(input())
        sumaNotasSalon = sumaNotasSalon + nota
        sumaGlobal = sumaGlobal + nota
        totalAlumnos = totalAlumnos + 1
    promSalon = sumaNotasSalon / alumnos
    print("promedio del salon es " + str(promSalon))
promGlobal = sumaGlobal / totalAlumnos
print("promedio global es " + str(promGlobal))
