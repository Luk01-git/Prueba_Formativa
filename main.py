from Config.database import DatabaseManager
from Models.entidades import Departamento, Empleado, Proyecto
from Models.usuario import Usuario
from Views.views import VistaConsola

if __name__ == "__main__":
    db = DatabaseManager()
    db.conectar()
    db.crear_tablas_iniciales()
    
    vista = VistaConsola()

    # "Bases de datos" temporales en memoria (Diccionarios)
    usuarios_db = {}   # Guarda objetos Usuario vinculados al 'username'
    empleados_db = {}  # Guarda objetos Empleado vinculados al 'username'
    
    # Creamos un proyecto por defecto para tener donde registrar horas
    proyecto_renovable = Proyecto("P100", "Optimización Energética Fase 1")

    while True:
        # 1. MENÚ DE INICIO (Fuera del sistema)
        opcion_inicio = vista.mostrar_menu_inicio()
        
        if opcion_inicio == "1":
            # Flujo de Login
            if not usuarios_db:
                vista.mostrar_mensaje("No hay usuarios registrados. Por favor, registre uno primero.", "error")
                continue
                
            user, pwd = vista.mostrar_login()
            
            # Verificamos si existe el usuario y si la clave (hasheada) coincide
            if user in usuarios_db and usuarios_db[user].autenticar(pwd):
                vista.mostrar_mensaje("Sesión iniciada correctamente.", "exito")
                empleado_actual = empleados_db[user]
                
                # 2. MENÚ DE USUARIO (Dentro del sistema)
                while True:
                    opcion_usr = vista.mostrar_menu_usuario(user)
                    
                    if opcion_usr == "1":
                        vista.mostrar_mensaje(f"ID Empleado: {empleado_actual.get_idEmpleado()}")
                        vista.mostrar_mensaje(f"Salario Confidencial: ${empleado_actual.get_salario()}")
                        
                    elif opcion_usr == "2":
                        horas = vista.pedir_registro_horas()
                        if horas > 0:
                            try:
                                registro = empleado_actual.registrarHoras(proyecto_renovable, horas)
                                vista.mostrar_mensaje(
                                    f"Registraste {registro.horas} hrs en '{proyecto_renovable.nombre}'. "
                                    f"Total del proyecto: {proyecto_renovable.obtenerTotalHoras()} hrs.", 
                                    "exito"
                                )
                            except ValueError as error_negocio:
                                vista.mostrar_mensaje(str(error_negocio), "error")
                        else:
                            vista.mostrar_mensaje("Entrada inválida. Ingrese un valor positivo.", "error")
                            
                    elif opcion_usr == "3":
                        vista.mostrar_mensaje("Cerrando sesión...")
                        break
                    else:
                        vista.mostrar_mensaje("Opción no válida.", "error")
            else:
                vista.mostrar_mensaje("Credenciales incorrectas o usuario no existe.", "error")
                
        elif opcion_inicio == "2":
            # Flujo de Registro
            id_emp, nombre, correo, salario, username, password = vista.pedir_datos_empleado()
            
            if username in usuarios_db:
                vista.mostrar_mensaje("El nombre de usuario ya está en uso.", "error")
            else:
                # Instanciamos los nuevos objetos basados en tus modelos
                nuevo_usuario = Usuario(f"U-{id_emp}", username, password)
                nuevo_empleado = Empleado(id_emp, nombre, correo, salario)
                
                # Relación 1 a 1 entre Empleado y Usuario
                nuevo_empleado.set_usuario(nuevo_usuario)
                
                # Asignamos automáticamente al proyecto de prueba para que pueda registrar horas
                proyecto_renovable.asignarEmpleado(nuevo_empleado)
                
                # Guardamos en nuestros diccionarios temporales
                usuarios_db[username] = nuevo_usuario
                empleados_db[username] = nuevo_empleado
                
                vista.mostrar_mensaje(f"Empleado '{nombre}' registrado exitosamente.", "exito")

        elif opcion_inicio == "3":
            vista.mostrar_mensaje("Apagando sistema EcoTech...")
            db.cerrar_conexion()
            break
            
        else:
            vista.mostrar_mensaje("Opción no válida. Intente nuevamente.", "error")
