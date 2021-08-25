import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f'\nOk {usuario[1]}!! vamos a crear una nota...')
        titulo = input('Introduce un titulo para tu nota: ')
        descripcion = input('introduce el contenido de tu nota: ')

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f'\nPerfecto has creado la nota {nota.titulo}')
        
        else:
            print(f'No se ha podido crear la nota, lo sentimos {usuario[1]}')
    
    def mostrar(self, usuario):
        print(f'\nOk {usuario[1]}!! aqui tienes tus notas...')

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print('----------------------------------------------------------')
            print(f'Título: {nota[2]}')
            print(f'\nContenido: {nota[3]}')
            print('----------------------------------------------------------')
    
    def borrar(self, usuario):
        print(f'Ok {usuario[1]} vamos a borrar notas!!')

        titulo = input('\nIntroduce el titulo de la nota a borrar :')
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print('\nHas eliminado la nota correctamente!!')

        else:
            print('\nNo se ha podido eliminar la nota!!')