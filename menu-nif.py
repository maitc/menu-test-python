def grabarCiudadano(ciudadano):
    print(ciudadano)
    valida = True
    print('Has ingresado a la opción de registrar un ciudadano: ')
    preguntar = input('Desea ingresar un nuevo ciudadano (S/N): \r\n')

    while preguntar == 's' or preguntar == 'S':
        nif = int(input('Registre su NIF sin dígito verificador: '))
        nifDigitoVerificador = input('Registre su dígito verificador de su NIF sin guión: ')

        while valida:
            try:
                nombre = input('Registre nombre: ')
                if len(nombre) >= 8:
                    valida = False
                else:
                    print('El nombre debe tener mínimo 8 carácteres')
            except:
                print('Debes ingresar un nombre')
        valida = True

        diaNacimiento = int(input('Registre día de nacimiento: '))
        mesNacimiento = int(input('Registre mes de nacimiento: '))

        while valida:
            try:
                anioNacimiento = int(input('Registre año de nacimiento: '))
                if anioNacimiento < 2022:
                    valida = False
                else:
                    print('Debe ser mayor a 0')
            except:
                print('El año es un número')
        valida = True

        estadoConyugal = input('Registre su estado conyugal: ')

        preguntar = input('Desea ingresar un nuevo ciudadano (S/N): \r\n')
    
    fechaNacimiento = f'{diaNacimiento}/{mesNacimiento}/{anioNacimiento}'
    nifCompleto = f'{nif}-{nifDigitoVerificador}'

    ciudadano[f'{nif}'] = [nif, nifDigitoVerificador, nombre, fechaNacimiento, estadoConyugal]
    

ciudadanos = {}

def buscarCiudadanos(*args):
    print('Estas en consultar datos de un ciudadano')
    nif = int(input('Ingrese el NIF sin dígito verificador: '))
    for ciudadano in args:
        if ciudadano.get(f'{nif}'):
            print(ciudadano)
        else:
            print('El nif no esta en nuestros registros')


def printCertificado(*args):
    nif = int(input('Ingrese el NIF sin dígito verificador: '))
    for ciudadano in args:
        if ciudadano.get(f'{nif}'):
            ciud = ciudadano.get(f'{nif}')
            print('CERTIFICADO REGISTRO CIVIL')
            print('')
            print(f'NIF: {ciud[0]}/{ciud[1]}')
            print(f'Nombre: {ciud[2]}')
            print(f'Fecha nacimiento: {ciud[3]}')
            print(f'Estado conyugal: {ciud[4]}')
            print('')


def baseCiudadanos():
    valida = True
    while(True):
        
        print('Bienvenido al registro de ciudadanos')
        print('1.- Registrar ciudadano')
        print('2.- Buscar ciudadano')
        print('3.- Imprimir certificado')
        print('4.- Salir')

        opcion = int(input('Ingrese opción: '))

        if(opcion == 1):
            print('Has ingresado a registrar un ciudadano')
            grabarCiudadano(ciudadanos)
        elif(opcion == 2):
            print('Has ingresado a buscar ciudadano')
            buscarCiudadanos(ciudadanos)
        elif(opcion == 3):
            print('Has ingresado a imprimir certificado')
            printCertificado(ciudadanos)
        elif(opcion == 4):
            print('Gracias por usar nuestro sistema')
            break
        else:
            print('Ingrese una opción valida')

        
baseCiudadanos()