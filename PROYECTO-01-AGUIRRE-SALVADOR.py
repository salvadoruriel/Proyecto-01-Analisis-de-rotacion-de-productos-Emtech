#Programa de Salvador Uriel Aguirre Andrade
# Bienvenida e ingreso de usuario para el analisis
print("**********************************")
print("Sistema de analisis para LifeStore")
print("**********************************")

#definicion de usuarios, ingreso y comprobacion de usuario
from lifestore_file import lifestore_searches, lifestore_products, lifestore_sales

#con userType 0 son usuarios, con 1 son admins
#osea 1,1 y LifeStore,admin son cuentas a usar
userType = ['user', 'admin']
usuarios = [['0', '0', userType[0]], ['1', '1', userType[1]],
            ['2', '2', userType[0]], ['3', '3', userType[0]],
            ['4', '4', userType[0]], ['LifeStore', 'admin', userType[1]]]
go = 0
while go == 0:
    found = 0
    while (found == 0):
        usuarioInput = input("Dame el usuario: ")
        for user in usuarios:
            if (usuarioInput == user[0]):
                found = 1
                break
        if (found == 0): print("El usuario no existe")

    #ingreso y comprobacion de contraseña
    found = 0
    while (found == 0):
        passwordInput = input("Ingresa la contraseña: ")
        if (passwordInput == user[1]):
            found = 1
        if (found == 0): print("Contraseña incorrecta.")

    if user[2] == userType[0]:
        print(">>Como usuario no tiene permiso para ver esta informacion")
        print("----------------------------------")
        continue
    go = 1

#ingreso de opciones y entrega de analisis
opcion = 0
while (opcion != 'q'):
    print("----------------------------------")
    print("Seleccione reporte a mostrar: ")
    print("1 - Productos más vendidos y productos rezagados")
    print("2 - Productos por reseña en el servicio")
    print(
        "3 - Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año"
    )
    #ya que no podemos usar funciones esta opcion ya no sera
    #print("5 - Todos los anteriores (en orden)")
    print("q - Salir")
    opcion = input("--> ")

    if (opcion == '1'):
        while (opcion != 'b'):
            print("----------------------------------")
            print("Listas: ")
            print("1 - Más vendidos y más buscados")
            print("2 - Rezagados (por categoria)")
            print("b - regresar")
            opcion = input("--> ")

            if opcion == '1':
                print("----------------------------------")
                #generar listado  de los 50 productos con mayores ventas
                lista_ventas = []
                #lleno la lista con los pares que ya voy a utilizar
                #formato [venta, reembolsos, productoId]
                for indx in range(0, len(lifestore_products)):
                    lista_ventas.append([0, 0, indx + 1])
                for compra in lifestore_sales:
                    #agrego valor, en compra 1 es id producto, 4 es reembolso
                    if (compra[4] == 1):  #reembolso
                        lista_ventas[compra[1]][1] += 1
                    """"
              if (compra[1] >= len(lista_ventas)):  #considero un orden con el id
                  lista_ventas.append([1, compra[1]])
              else:  #considero compras ordenadas por prod_id
                  lista_ventas[compra[1]][0] += 1  #[cant +=1, id]
              """
                    lista_ventas[compra[1]][0] += 1  #[cant +=1, id]
                #ordena segun el 1er elemento en arreglos dobles
                lista_ventas.sort(reverse=True)
                #print(lista_ventas)
                print(">>>Los 50 productos mas vendidos: ")
                #total = 0
                maxRang = 51 if 50 <= len(lifestore_products) else len(
                    lifestore_products)
                for num in range(1, maxRang):
                    productoId = lista_ventas[num - 1][2]
                    compras = lista_ventas[num - 1][0]
                    reembolsos = lista_ventas[num - 1][1]
                    name = lifestore_products[productoId - 1][1]
                    #total += compras
                    #en lifestore_products 1 es name
                    #print(num, '. (ventas: ', compras, ') ', "||", productoId, end=' ')
                    if reembolsos == 0:
                        print(num, '. (ventas: ', compras, ' ) ', name, sep='')
                    else:
                        print(
                            num,
                            '. (ventas: ',
                            compras,
                            ' | reembolsos: ',
                            reembolsos,
                            ' ) ',
                            name,
                            sep='')
                    if compras == 0: break
                #print(total)
                print("----------------------------------")

                #listado con los 100 productos con mayor búsquedas
                lista_busquedas = []
                #similarmente hago un acomodo primero tomando indice como id
                for indx in range(0, len(lifestore_products)):
                    lista_busquedas.append([0, indx + 1])
                for busqueda in lifestore_searches:
                    lista_busquedas[busqueda[1]][0] += 1
                #ahora si ordeno y uso el indice en 2da posicion, como en la vez anterior
                lista_busquedas.sort(reverse=True)
                #print(lista_busquedas)
                maxRang = 101 if 100 <= len(lifestore_products) else len(
                    lifestore_products)
                print(">>>Los 100 productos mas buscados: ")
                for num in range(1, maxRang):
                    productoId = lista_busquedas[num - 1][1]
                    busquedas = lista_busquedas[num - 1][0]
                    name = lifestore_products[productoId - 1][1]
                    #en lifestore_products 1 es name
                    print(num, '. (busquedas: ', busquedas, ') ', name, sep='')
                    if busquedas == 0: break
                print('************************************************')
                print('************************************************')
                print('Fin del primer reporte:')
                print('1.1 Productos más vendidos y más buscados')
                print('************************************************')
                print('************************************************')

            elif opcion == '2':
                """
                print("----------------------------------")
                print("----------------------------------")
                print("--------Producto rezagado---------")
                print("----------por categoria-----------")
                print("----------------------------------")
                print("----------------------------------")
                print("------------VENTAS----------------")
                print("------------vvvvvv----------------")
                """
                print("----------------------------------")
                #Por categoría, generar un listado con los 50 productos con menores ventas y uno con los 100 productos con menores búsquedas.
                categories = []
                #genero las categorias que hay segun los productos
                for product in lifestore_products:
                    #en 3 esta la categoria
                    if not (product[3] in categories):
                        categories.append(product[3])
                #reordeno la lista pero sin estar en reversa
                lista_ventas.sort()
                for cat in categories:
                    print("Las(os) 50", cat, "menos vendidos(as).")
                    num = 1
                    for venta in lista_ventas:
                        if num > 50: break
                        #checo si no esta en la categoria el producto
                        prodId = venta[2]
                        if lifestore_products[prodId - 1][3] != cat: continue
                        #ahora si imprimo elemento de la lista, 1 es name
                        name = lifestore_products[prodId - 1][1]
                        print(num, '. (ventas: ', venta[0], ') ', name, sep='')
                        num += 1
                    print("----------------------------------")
                    """ #iba a rehacer las busquedas pero lo de arriba es mas rapido/optimo
              lista_ventas=[]
              #ahora lleno la lista con los productos de la categoria
              for product in lifestore_products:
                if product[3] == cat:
                  lista_ventas.append([0,product[0]])
              for compra in lifestore_sales:
                  if (compra[4] == 1):  #reembolsos se omiten
                      continue
                  prodId = compra[1]
              """
                #y uno con los 100 menos buscados
                print("------------BUSQUEDAS-------------")
                print("------------vvvvvvvvv-------------")
                lista_busquedas.sort()
                #resuelvo similarmente
                for cat in categories:
                    print("Las(os) 50", cat, "menos buscadas(os).")
                    num = 1
                    for busqueda in lista_busquedas:
                        if num > 50: break
                        #checo si no esta en la categoria el producto
                        prodId = busqueda[1]
                        if lifestore_products[prodId - 1][3] != cat: continue
                        #ahora si imprimo elemento de la lista, 1 es name
                        name = lifestore_products[prodId - 1][1]
                        print(
                            num,
                            '. (busquedas: ',
                            busqueda[0],
                            ') ',
                            name,
                            sep='')
                        num += 1
                    print("----------------------------------")
                print('************************************************')
                print('************************************************')
                print('Fin del primer reporte:')
                print('1.2 Productos rezagados')
                print('************************************************')
                print('************************************************')

            elif opcion == 'b':
                print("Regresando...")
            else:
                print(opcion + " no esta en el menu")

    elif (opcion == '2'):
        #Mostrar dos listados de 20 productos cada una, un listado para productos con las mejores reseñas y otro para las peores, considerando los productos con devolución.
        lista_resenias = []
        for producto in lifestore_products:
            #acomodo puntuacion, total resenias, y finalmente id
            lista_resenias.append([0, 0, producto[0]])
        #uso tecnica similar, con indice inicilamente en misma posicion que prod_id
        for sale in lifestore_sales:
            #como considero los productos aun devueltos, comento la linea de abajo
            #if sale[4] == 1: continue
            calif = sale[2]
            prodId = sale[1]
            lista_resenias[prodId - 1][0] += calif
            lista_resenias[prodId - 1][1] += 1
        for res in lista_resenias:
            if res[1] == 0: continue
            res[0] /= res[1]
        #ahora si ya ordeno e imprimo
        print("----------------------------------")
        tamanio_lista = 20
        print(">>>Los", tamanio_lista, "productos con mejores reseñas: ")
        lista_resenias.sort(reverse=True)
        for num in range(1, tamanio_lista + 1):
            calif = lista_resenias[num - 1][0]
            prodId = lista_resenias[num - 1][2]
            nombre = lifestore_products[prodId - 1][1]
            print(
                num,
                '. (calificación: ',
                round(calif, 2),
                ') ',
                nombre,
                sep='')
        print("----------------------------------")
        print("----------------------------------")
        tamanio_lista = 20
        print(">>>Los", tamanio_lista, "productos con peores reseñas: ")
        lista_resenias.sort()
        """"
        for num in range(1, tamanio_lista + 1):
            #si no hay resenias, lo omito, ya que muchos se quedan en 0
            #y/o no tiene sentido si aun no se ha vendido
            if lista_resenias[num - 1][1] == 0: continue
            calif = lista_resenias[num - 1][0]
            prodId = lista_resenias[num - 1][2]
            name = lifestore_products[prodId - 1][1]
            print(
                num, '. (calificación: ', round(calif, 2), ') ', name, sep='')
        """
        num = 1
        for res in lista_resenias:
            #si no hay resenias, lo omito, ya que muchos se quedan en 0
            #y/o no tiene sentido si aun no se ha vendido
            if num > tamanio_lista: break
            if res[1] == 0: continue
            calif = res[0]
            prodId = res[2]
            name = lifestore_products[prodId - 1][1]
            print(
                num, '. (calificación: ', round(calif, 2), ') ', name, sep='')
            num += 1
        print('************************************************')
        print('************************************************')
        print('Fin del segundo reporte:')
        print('2. Productos por reseña en el servicio')
        print('************************************************')
        print('************************************************')

    elif (opcion == '3'):
        #Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al anio
        years = []
        for sale in lifestore_sales:
            datestring = sale[3]
            year = datestring[6:]
            #3 es la fecha, formato ejemplo: '24/07/2020'
            if not year in years:
                years.append(year)

        meses = [
            'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
            'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ]
        for year in years:
            months_sales = []
            months_refunds = []
            months_earnings = []
            for mes in meses:
                #formato [venta/ganancias, mes]
                months_sales.append([0, mes])
                months_earnings.append([0, mes])
                months_refunds.append([0, mes])
            totalIngresos = 0
            #years.append([year, 0, months_sales, months_earnings])
            for sale in lifestore_sales:
                datestring = sale[3]
                yearstr = datestring[6:]
                if yearstr != year: continue
                #datos a usar
                month = datestring[3:5]
                idProd = sale[1]
                precio = lifestore_products[idProd - 1][2]
                #meses en orden
                idxmonth = int(month) - 1
                months_sales[idxmonth][0] += 1
                months_earnings[idxmonth][0] += precio
                totalIngresos += precio
                if sale[4] == 1:
                    months_refunds[idxmonth][0] += 1
            print("***********************************")
            print("****** Reporte del año", year, "*******")
            vetans_prommensuales = 0
            gains_prommensuales = 0
            for num in range(0, 12):
                vetans_prommensuales += months_sales[num][0]
                gains_prommensuales += months_earnings[num][0]
            vetans_prommensuales /= 12
            gains_prommensuales /= 12
            print(">Promedio de ventas mensuales:",
                  round(vetans_prommensuales, 2))
            print(
                ">Promedio de ganancias mensuales: $",
                round(gains_prommensuales, 2),
                sep='')
            print(">Total de ingresos: $", totalIngresos, sep='')
            print("----Meses con mas ventas--")
            months_sales.sort(reverse=True)
            #print(months_sales)
            for num in range(0, 12):
                ventas = months_sales[num][0]
                mes = months_sales[num][1]
                print(num + 1, '. (ventas: ', ventas, ') ', mes, sep='')
                if ventas == 0: break
            print("----Meses con mas ganancias--")
            months_earnings.sort(reverse=True)
            #print(months_earnings)
            for num in range(0, 12):
                ingreso = months_earnings[num][0]
                mes = months_earnings[num][1]
                print(num + 1, '. (ingreso: $', ingreso, ') ', mes, sep='')
                if ingreso == 0: break
            print("----Meses con mas reembolsos--")
            months_refunds.sort(reverse=True)
            #print(months_earnings)
            for num in range(0, 12):
                reemb = months_refunds[num][0]
                mes = months_refunds[num][1]
                print(num + 1, '. (reembolsos: ', reemb, ') ', mes, sep='')
                if reemb == 0: break

        print('************************************************')
        print('************************************************')
        print('Fin del tercer reporte:')
        print(
            '3. Total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año'
        )
        print('************************************************')
        print('************************************************')
    #elif (opcion == '5'):
    #    print("wip")
    elif (opcion == 'q'):
        print("Desconectado...")
    else:
        print(opcion + " no esta en el menu")
