"""
Proyecto Python y Mysql
-Abrir asistente
-Login o registro
-Si elegimos login, identifica al usuario y nos preguntará
-Crear notas, mostrar notas y borrarlas.
"""

from usuarios import acciones

print('''
Acciones disponibles:
    -registro
    -login
''')

HazEl = acciones.Acciones()

accion = input('¿Que acción quieres hacer?')

if accion == 'registro':
    HazEl.registro()
    

elif accion == 'login':
    HazEl.login()
    