sumaGlobal = 0
totalAlumnos = 0
i = 1
print("ingrese numero de salones ")
salones = int(input())
while i <= salones:
    sumaNotasSalon = 0
    j = 1
    print("Ingrese  alumnos de este salon")
    alumnos = int(input())
    while j <= alumnos:
        print("ingrese nota del estudiante")
        nota = float(input())
        sumaNotasSalon = sumaNotasSalon + nota
        sumaGlobal = sumaGlobal + nota
        totalAlumnos = totalAlumnos + 1
        j = j + 1
    promSalon = sumaNotasSalon / alumnos
    print("promedio del salon es " + str(promSalon))
    i = i + 1
promGlobal = sumaGlobal / totalAlumnos
print("promedio global es " + str(promGlobal))
