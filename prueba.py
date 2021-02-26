marcas = {'Ford':100000, 'Chevrolet':120000, 'Fiat':80000}
puertas = {'2':50000, '4':65000, '5':78000}
colores = {'blanco':10000, 'azul':20000, 'negro':30000}

#funcion para el descuento
def descuento(cantidad_de_clientes, precio_final_de_cliente):
    if(cantidad_de_clientes < 6):
        precio_final_de_cliente = precio_final_de_cliente
    elif(cantidad_de_clientes >= 6 and cantidad_de_clientes <= 10):
        precio_final_de_cliente = precio_final_de_cliente-(precio_final_de_cliente *10)/100
    elif(cantidad_de_clientes > 10 and cantidad_de_clientes <= 50):
        precio_final_de_cliente = precio_final_de_cliente-(precio_final_de_cliente *15)/100
    elif(cantidad_de_clientes > 50):
        precio_final_de_cliente = precio_final_de_cliente-(precio_final_de_cliente *18)/100
    return precio_final_de_cliente

numero_cliente = 0
cliente = {}
otro_cliente_comprobacion = True
while(otro_cliente_comprobacion == True):
    nombre = input('Nombre:')
    apellido = input('Apellido:')
    marca = input('Marca:')

    precio_final = 0
    #marca
    marca_existe = False
    while(marca_existe == False):
        if(marca in marcas):
            marca_existe = True
            precio_final += marcas[marca]
        else:
            print('elija una marca entre Ford, Chevrolet o Fiat')
            marca = input('Marca:')
            marca_existe = False
    #puerta
    puerta = input('Puertas:')
    puerta_existe = False
    while(puerta_existe == False):
        if(puerta in puertas):
            puerta_existe = True
            precio_final += puertas[puerta]
        else:
            print('elija una cantidad de puertas entre 2, 4 y 5')
            puerta = input('Puertas:')
            puerta_existe = False
    #color
    color = input('Color:')
    color_existe = False
    while(color_existe == False):
        if(color in colores):
            color_existe = True
            precio_final += colores[color]
        else:
            print('elija un color entre blanco, azul y negro')
            color = input('Color:')
            color_existe = False

   
    
    #armo los array

    cliente[numero_cliente] = [nombre,apellido,marca,puerta,color,precio_final]
  #  print('numero de cliente'+str(numero_cliente))
   # print(cliente[numero_cliente][5])
     #otro cliente
    otro_cliente = input('Habra otro cliente:')
    otro_cliente_loop_para_error = False
    while(otro_cliente_loop_para_error == False):
        if(otro_cliente != 'si' and otro_cliente != 'no'):
            print('elija si o no')
            otro_cliente = input('Habra otro cliente:') 
            otro_cliente_loop_para_error = False
        elif(otro_cliente == 'si'):
            otro_cliente_comprobacion = True   
            otro_cliente_loop_para_error = True
            numero_cliente += 1
        else:
           otro_cliente_loop_para_error = True
           otro_cliente_comprobacion = False
#print('numero de cliente'+str(numero_cliente))
#aca imprimo con el descuento
for i in range(numero_cliente+1):
    cliente[i][5] = descuento(numero_cliente,cliente[i][5])
   # print('numero de cliente:'+str(numero_cliente))
   # print('nombre:'+str(cliente[i][0]))
    print('El cliente '+str(cliente[i][0])+' '+str(cliente[i][1])+' se compro un auto marca '+str(cliente[i][2])+' con '+str(cliente[i][3])+' puertas y de color '+str(cliente[i][4])+' a un precio de '+str(cliente[i][5])+' _______  ')
