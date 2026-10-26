class VistaConsola:
    def mostrar_menu_inicio(self):
        print("\n" + "="*40)
        print("   SISTEMA ECOTECH - INICIO")
        print("="*40)
        print("1. Iniciar sesión")
        print("2. Registrar nuevo empleado")
        print("3. Salir del sistema")
        return input("Seleccione una opción (1-3): ")

    def pedir_datos_empleado(self):
        print("\n--- REGISTRO DE NUEVO EMPLEADO ---")
        id_emp = input("ID Empleado (ej. E002): ")
        nombre = input("Nombre completo: ")
        correo = input("Correo corporativo: ")
        try:
            salario = float(input("Salario bruto: $"))
        except ValueError:
            salario = 0.0
            print("[-] Salario inválido, se registró como $0.0")
            
        username = input("Nombre de usuario para el sistema: ")
        password = input("Contraseña: ")
        return id_emp, nombre, correo, salario, username, password

    def mostrar_login(self):
        print("\n--- INICIO DE SESIÓN ---")
        username = input("Usuario: ")
        password = input("Contraseña: ")
        return username, password

    def mostrar_menu_usuario(self, nombre_usuario):
        print(f"\n--- PANEL DE CONTROL: {nombre_usuario} ---")
        print("1. Ver mis datos laborales")
        print("2. Registrar horas trabajadas en proyecto")
        print("3. Cerrar sesión")
        return input("Seleccione una opción (1-3): ")

    def pedir_registro_horas(self):
        print("\n--- NUEVO REGISTRO DE HORAS ---")
        try:
            horas = float(input("Ingrese la cantidad de horas a registrar: "))
            return horas
        except ValueError:
            return -1.0

    def mostrar_mensaje(self, mensaje: str, tipo: str = "info"):
        if tipo == "error":
            print(f"[!] ERROR: {mensaje}")
        elif tipo == "exito":
            print(f"[*] ÉXITO: {mensaje}")
        else:
            print(f"[-] {mensaje}")
