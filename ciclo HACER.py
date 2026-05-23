sumaGlobal = 0
totalAlumnos = 0
i = 1
print("ingrese numero de salones ")
salones = int(input())
while True:    #This simulates a Do Loop
    print("Ingrese  alumnos de este salon")
    alumnos = int(input())
    sumaNotasSalon = 0
    j = 1
    while True:    #This simulates a Do Loop
        print("ingrese nota del estudiante")
        nota = float(input())
        sumaNotasSalon = sumaNotasSalon + nota
        sumaGlobal = sumaGlobal + nota
        totalAlumnos = totalAlumnos + 1
        j = j + 1
        if j > alumnos: break  # noqa: E701
    promSalon = sumaNotasSalon / alumnos
    print("promedio del salon es " + str(promSalon))
    i = i + 1
    if i > salones: break  # noqa: E701
promGlobal = sumaGlobal / totalAlumnos
print("promedio global es " + str(promGlobal))
