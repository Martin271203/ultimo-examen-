
productos = {'0001':['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '0002':['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
             '0003':['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX280ti'],
             '0004':['HP', 15.6, '12GB', 'DD', '1T', 'Intel i5', 'Integrada'],
             '0005':['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
             '0006':['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'Integrada'],
             '0007':['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvdia GTX1050'],
             '0008':['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX 1050'],
             '0009':['Asus', 14, '16GB', 'SDD', '1T', 'AMD Ryzen 9', 'Nvidia RTX 5090'],
             }




stock = {'0001':[390990,10],
         '0002':[329990,4], 
         '0003': [429990,1], 
         '0004': [652990,21], 
         '0005': [299990,32], 
         '0006': [449990,7], 
         '0007': [1200990,2], 
         '0008': [259990,1], 
         '0009': [5120990,0]
         }




def stock_marca(marca):
    total_stock = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            total_stock += stock[modelo][1]
    print(f"Stock total de la marca {marca}: {total_stock}")

def busqueda_precio(p_min, p_max):
    if not (isinstance(p_min, int) and isinstance(p_max, int)):
        print("Debe ingresar valores enteros!!")
        return
    encontrados = []
    for modelo, (precio, cantidad) in stock.items():
        if p_min <= precio <= p_max:
            marca = productos[modelo][0]
            encontrados.append(f"{marca}–{modelo}")
    if encontrados:
        encontrados.sort()
        for item in encontrados:
            print(item)
    else:
        print("No hay notebooks en ese rango de precios")

def ordenar_productos():
    if not productos:
        print("No hay notebook disponibles")
        return
    lista = []
    for modelo, datos in productos.items():
        marca, pantalla, ram, disco, gb, *_ = datos
        lista.append((marca, f"{marca} - {modelo} - {ram} - {disco} - {gb}"))
    lista.sort()
    for _, info in lista:
        print(info)

def menu():
    while True:
        print("\n* MENU PRINCIPAL *")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Listado de productos.")
        print("4. Salir.")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            marca = input("Ingrese la marca: ")
            stock_marca(marca)
        elif opcion == '2':
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                busqueda_precio(p_min, p_max)
            except ValueError:
                print("Debe ingresar valores enteros")
        elif opcion == '3':
            ordenar_productos()
        elif opcion == '4':
            print("Programa finalizado")
            break
        else:
            print("Debe seleccionar otra")
            
menu()