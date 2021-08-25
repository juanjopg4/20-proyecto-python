import usuarios.usuario as modelo
import notas.acciones
class Acciones:

    def registro(self):
        print('\nOk!! Vamos a registrarte en el sistema...')

        nombre = input('¿Cual es tu nombre?: ')
        apellidos = input('¿Cuales son tus apellidos?: ')
        email = input('Introduce tu gmail: ')
        password = input('introduce tu contraseña: ')

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f'\nperfecto {registro[1].nombre} te has registrado correctamente!!')
        
        else:
            print(f'\nLo sentimos {registro[1].nombre} no te has registrado correctamente!!')

    def login(self):
        print('\nVale!! Identificate en el sistema...')

        nose = 0
        while nose == 0:
            try:

                email = input('\nIntroduce tu gmail: ')
                password = input('introduce tu contraseña: ')

                usuario = modelo.Usuario('','',email,password)
                login = usuario.identificar()

                if login[3] == email:
                    nose += 1
                    print(f'Enhorabuena {login[1]} te has identificado correctamente!!')
                    self.proximasAcciones(login)
                        
            except Exception:
                print('Los datos introducidos no son validos, vuelva a intentarlo')

    def proximasAcciones(self, usuario):
        print('''
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar nota (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        ''')
        accion = input('\n¿Que quieres hacer?: ')
        HazEl = notas.acciones.Acciones()


        if accion == 'crear':
            HazEl.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == 'mostrar':
            HazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == 'eliminar':
            HazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'salir':
            print(f'Ok {usuario[1]} hasta pronto!!')
            exit()
