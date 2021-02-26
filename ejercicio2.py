#Dada una concesionaria de autos, 5 clientes van a pedir un auto, debe preguntarsele:
#inputs
#marcas y precios
precio_ford = 100000
precio_chevrolet = 120000  
precio_fiat = 80000

#precios puertas
precio_puertas2 = 50000
precio_puertas4 = 65000
precio_puertas5 = 78000

#precios color
precio_blanco = 10000
precio_azul = 20000
precio_negro = 30000
for i in range(5):
    precio_final = 0
    nombre = input('Nombre:')
    apellido = input('Apellido:')
    marca = input('Marca de su coche:')
    puertas = input('Cantidad de puertas:')
    color = input('Color del coche:')

    #Deben imprimirse los datos de cada compra y el precio total.
    if(marca != 'Ford' and marca != 'Chevrolet' and marca != 'Fiat'):
        print('introduzca una marca valida entre Ford, Chevrolet o Fiat')
    elif(puertas != '2' and puertas != '4' and puertas != '5'):
        print('introduzca una cantidad de puertas validas entre 2, 4 y 5')
    elif(color != 'blanco' and color != 'azul' and color != 'negro'):
        print('introduzca un color valido entre blanco, azul o negro')
    else:
        if(marca == 'Ford'):
            precio_final = precio_ford    
        if(marca == 'Chevrolet'):
            precio_final = precio_chevrolet
        if(marca == 'Fiat'):
            precio_final = precio_fiat
        if(puertas == '2'):
            precio_final = precio_final+precio_puertas2
        if(puertas == '4'):
            precio_final = precio_final+precio_puertas4
        if(puertas == '5'):
            precio_final = precio_final+precio_puertas5
        if(color == 'blanco'):
            precio_final = precio_final+precio_blanco
        if(color == 'azul'):
            precio_final = precio_final+precio_azul
        if(color == 'negro'):
            precio_final = precio_final+precio_negro        
        
        print(nombre+' '+apellido+' esta comprando un '+marca+' y ha seleccionado '+ str(puertas) +' puertas y que sea de color '+color+' y todo esto le costara:'+str(precio_final))