def agregar_compra(compras):
    compra= (float(input("Ingresa el monto de la compra: ")))
    compras.append(compra)
    print("Compra agregada correctamente.")

def mostrar_compras(compras):
    if len(compras) ==0:
        print("No hay compras registradas")
    else:
        for i, num in enumerate(compras,+1):
            print(f"Compra {i} monto ${num}")

def mostrar_total(compras):
    total_gastado = format(sum(compras))
    print(f"Total gastado: ${total_gastado}")

def main():
    compras=[]
    total_gastado=0
    while True:
        print("1. Agregar Compra")
        print("2. Mostar Compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        opcion= int(input("Seleccione una opcion: "))
        if opcion == 1:
            agregar_compra(compras)
        elif opcion == 2:
            mostrar_compras(compras)
        elif opcion == 3:
            mostrar_total(compras)
        else:
            print("¡Hasta luego!")
            break

main()
