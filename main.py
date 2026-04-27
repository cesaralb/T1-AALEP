class Puesto:
    def __init__(self, codigo, descripcion, areaSolicitante, plazasRequeridas, sueldo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.areaSolicitante = areaSolicitante
        self.plazasRequeridas = plazasRequeridas
        self.sueldo = sueldo

listaPuestos = []

def MostrarTodo():
    for p in listaPuestos:
        print(p.codigo, p.descripcion, p.areaSolicitante, p.plazasRequeridas, p.sueldo)

def AgregaPuesto():
    codigo = int(input("Codigo: "))
    descripcion = input("Descripcion: ")
    area = input("Area: ")
    plazas = int(input("Plazas: "))
    sueldo = float(input("Sueldo: "))

    if len(descripcion) < 3 or len(area) < 3:
        print("Error en texto")
        return

    if codigo <= 0 or plazas <= 0 or sueldo <= 0:
        print("Error en numeros")
        return

    for p in listaPuestos:
        if p.codigo == codigo or p.descripcion == descripcion or p.areaSolicitante == area:
            print("Ya existe")
            return

    nuevo = Puesto(codigo, descripcion, area, plazas, sueldo)
    listaPuestos.append(nuevo)
    print("Agregado")

def ordenarBurbuja():
    n = len(listaPuestos)
    for i in range(n):
        for j in range(0, n - 1):
            if listaPuestos[j].codigo < listaPuestos[j+1].codigo:
                aux = listaPuestos[j]
                listaPuestos[j] = listaPuestos[j+1]
                listaPuestos[j+1] = aux

def BorraPuesto():
    codigo = int(input("Codigo a eliminar: "))
    ordenarBurbuja()

    for i in range(len(listaPuestos)):
        if listaPuestos[i].codigo == codigo:
            listaPuestos.pop(i)
            print("Eliminado")
            return

    print("No encontrado")

def ordenarInsercion():
    for i in range(1, len(listaPuestos)):
        aux = listaPuestos[i]
        j = i - 1

        while j >= 0 and listaPuestos[j].sueldo < aux.sueldo:
            listaPuestos[j+1] = listaPuestos[j]
            j -= 1

        listaPuestos[j+1] = aux

def BuscaSueldo():
    sueldo = float(input("Sueldo a buscar: "))
    ordenarInsercion()

    izq = 0
    der = len(listaPuestos) - 1
    pos = -1

    while izq <= der:
        mid = (izq + der) // 2

        if listaPuestos[mid].sueldo == sueldo:
            pos = mid
            break
        elif listaPuestos[mid].sueldo < sueldo:
            der = mid - 1
        else:
            izq = mid + 1

    if pos == -1:
        print("No encontrado")
        return

    i = pos
    while i >= 0 and listaPuestos[i].sueldo == sueldo:
        print(listaPuestos[i].codigo, listaPuestos[i].sueldo)
        i -= 1

    i = pos + 1
    while i < len(listaPuestos) and listaPuestos[i].sueldo == sueldo:
        print(listaPuestos[i].codigo, listaPuestos[i].sueldo)
        i += 1

def ordenarSeleccion():
    n = len(listaPuestos)

    for i in range(n):
        max = i
        for j in range(i + 1, n):
            totalJ = listaPuestos[j].plazasRequeridas * listaPuestos[j].sueldo
            totalMax = listaPuestos[max].plazasRequeridas * listaPuestos[max].sueldo

            if totalJ > totalMax:
                max = j

        aux = listaPuestos[i]
        listaPuestos[i] = listaPuestos[max]
        listaPuestos[max] = aux

def PuestosAContratar():
    monto = float(input("Monto total: "))
    ordenarSeleccion()

    suma = 0

    for p in listaPuestos:
        total = p.plazasRequeridas * p.sueldo

        if suma + total <= monto:
            print(p.codigo, total)
            suma += total

listaPuestos.append(Puesto(1, "Dev", "Sistemas", 2, 2000))
listaPuestos.append(Puesto(2, "Tester", "Sistemas", 1, 1500))
listaPuestos.append(Puesto(3, "Recursos", "RRHH", 1, 1800))
listaPuestos.append(Puesto(4, "Contador", "Finanzas", 2, 2200))
listaPuestos.append(Puesto(5, "Soporte", "Sistemas", 3, 1200))
listaPuestos.append(Puesto(6, "Gerente", "Admin", 1, 5000))

while True:
    print("\n1 Agregar")
    print("2 Mostrar")
    print("3 Borrar")
    print("4 Buscar sueldo")
    print("5 Contratar")
    print("6 Salir")

    op = input("Opcion: ")

    if op == "1":
        AgregaPuesto()
    elif op == "2":
        MostrarTodo()
    elif op == "3":
        BorraPuesto()
    elif op == "4":
        BuscaSueldo()
    elif op == "5":
        PuestosAContratar()
    elif op == "6":
        break