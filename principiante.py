#Ingresar el nombre y apellido de un alumno y sus notas de matemática, literatura y física.
#Se pide imprimir el nombre, el apellido y el promedio.
#Si el promedio es mayor a 6 entonces debe aparecer un cartel que diga "Aprobado". Caso contrario, si tiene menos de 4 puntos imprimir "Insuficiente" y si tiene entre 4 y 5.99999 imprimir "A recuperatorio".
#En caso de tener 9 puntos o más, imprimir (aparte del aprobado) "Alumno destacado".

nombre = input('Nombre: ')
apellido = input('Apellido: ')
matematica = input('Nota Matematica: ')
literatura = input('Nota Literatura: ')
fisica = input('Fisica: ')
def promedio(mat, lit, fis):
    promedio_alumno = (int(mat)+int(lit)+int(fis))//3
    return promedio_alumno
if(matematica.isnumeric() and literatura.isnumeric() and fisica.isnumeric()):
      if(int(matematica)>10 or int(literatura)>10 or int(fisica)>10 ):
        print('numero ingresado no valido') 
      else:
        print(nombre +' '+ apellido +' tiene de promedio: '+ str(promedio(matematica, literatura, fisica)))
        if(promedio(matematica, literatura, fisica) >=6):
            print('Aprobado')
        elif(promedio(matematica, literatura, fisica) <4):
            print('Insuficiente')
        elif(promedio(matematica, literatura, fisica) >=4 and promedio(matematica, literatura, fisica)<6):
            print('a recuperatorio')
        if(promedio(matematica, literatura, fisica) >=9):
            print('Alumno destacado')

else:
    print('datos no validos, pruebe con numeros')
  