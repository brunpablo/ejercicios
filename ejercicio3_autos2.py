#Dado el problema anterior del concesionario de autos debemos modificarlo, teniendo en cuenta:

#1-Ya no sabemos cuantos clientes tendremos, 
#2-Si el pedido no es uno de los autos en venta, entonces debe volver a preguntar hasta que si lo sea
#3-Lo mismo con la cantidad de puertas y los colores.
#4-Al final se pregunta si hay otro cliente o no, si hay otro cliente, entonces vuelve a preguntar todo.
#5-Si la cantidad de clientes fue:
#--5.1: 0 a 5 personas no hay descuento
#--5.2: 6 a 10 personas: hay un descuento del 10%
#--5.3: 11 a 50 personas: hay un descuento del 15%
#--5.4: Más de 50 personas: El descuento es del 18%
#6-Solo se va a mostrar que se vendió al final del programa
#marcas y precios
marcas = {'Ford':100000, 'Chevrolet':120000, 'Fiat':80000}
#precios puertas
puertas = {'2':50000, '4':65000, '5':78000}
#precios color
colores = {'blanco':10000, 'azul':20000, 'negro':30000}
cantidad_clientes = 0
hay_otro_cliente = True
otro_cliente = 'si'
while(hay_otro_cliente == True):

    precio_final = 0
    nombre = input('Nombre:')
    apellido = input('Apellido:')
    marca = input('Marca de su coche:')

    if marca in marcas:
        precio_final += marcas[marca]
        puerta = input('Cantidad de puertas:')
        if puerta in puertas:
            precio_final += puertas[puerta]
            color = input('Color del coche:')
            if color in colores:
                precio_final += colores[color]
                print(nombre+' '+apellido+' compro un '+marca()+' de '+puerta+' puertas y de color'+color+' a un precio de'+precio_final)
                otro_cliente = input('Habra otro cliente:')
            else:
                print('solo hay blanco, azul y negro. intentelo nuevamente')
                color = input('Color del coche:')
        else:
            print('solo hay coches de 2 , 4 y 5 puertas. intentelo nuevamente')
            puerta = input('Cantidad de puertas:')
    else:
        print('no vendemos esa marca, solo Ford, Chevrolet o Fiat. intentelo nuevamente')
        marca = input('Marca de su coche:')
    

    if(otro_cliente == 'si'):
        hay_otro_cliente = True
    elif(otro_cliente == 'no'):
        hay_otro_cliente = False
    else:
        print('conteste si o no. intentelo nuevamente')
        otro_cliente = input('Habra otro cliente:')
