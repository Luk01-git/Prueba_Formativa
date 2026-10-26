from Config.database import DatabaseManager
from Models.entidades import Departamento, Empleado, Proyecto
from Models.usuario import Usuario
from Views.views import VistaConsola

if __name__ == "__main__":
    db = DatabaseManager()
    db.conectar()
    db.crear_tablas_iniciales()
    
    vista = VistaConsola()
    
    proyecto_renovable = Proyecto("P100", "Optimización Energética Fase 1")

    while True:
        opcion_inicio = vista.mostrar_menu_inicio()
        
        if opcion_inicio == "1":
            user, pwd = vista.mostrar_login()
            
            datos_bd = db.obtener_datos_login(user)
            
            if datos_bd:
                hash_bd, id_emp, nombre, correo, salario = datos_bd
                
                usuario_actual = Usuario(f"U-{id_emp}", user, hash_bd, is_hashed=True)
                
                if usuario_actual.autenticar(pwd):
                    vista.mostrar_mensaje("Sesión iniciada correctamente.", "exito")
                    
                    empleado_actual = Empleado(id_emp, nombre, correo, salario)
                    empleado_actual.set_usuario(usuario_actual)
                    proyecto_renovable.asignarEmpleado(empleado_actual)
                    
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
                    vista.mostrar_mensaje("Contraseña incorrecta.", "error")
            else:
                vista.mostrar_mensaje("El usuario no existe en la Base de Datos.", "error")
                
        elif opcion_inicio == "2":
            id_emp, nombre, correo, salario, username, password = vista.pedir_datos_empleado()
            
            nuevo_usuario = Usuario(f"U-{id_emp}", username, password)
            
            exito = db.registrar_empleado_y_usuario(
                id_emp, nombre, correo, salario,
                f"U-{id_emp}", username, nuevo_usuario.get_hash()
            )
            
            if exito:
                vista.mostrar_mensaje(f"Empleado '{nombre}' guardado permanentemente en la Base de Datos.", "exito")
            else:
                vista.mostrar_mensaje("El ID de Empleado o el Username ya están registrados en la BD.", "error")

        elif opcion_inicio == "3":
            vista.mostrar_mensaje("Apagando sistema EcoTech...")
            db.cerrar_conexion()
            break
            
        else:
            vista.mostrar_mensaje("Opción no válida. Intente nuevamente.", "error")
