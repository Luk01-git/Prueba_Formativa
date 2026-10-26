from datetime import date

class RegistroTiempo:
    def __init__(self, idRegistro: str, fecha: date, horas: float):
        self.__idRegistro = idRegistro
        self.__fecha = fecha
        self.__horas = horas

    @property
    def horas(self) -> float:
        return self.__horas

    def validarHoras(self) -> bool:
        return 0 < self.__horas <= 12

class Proyecto:
    def __init__(self, idProyecto: str, nombre: str):
        self.__idProyecto = idProyecto
        self.__nombre = nombre
        self.__empleados_asignados = [] 
        self.__registros_tiempo = []    

    @property
    def nombre(self) -> str:
        return self.__nombre

    def asignarEmpleado(self, empleado) -> None:
        if empleado not in self.__empleados_asignados:
            self.__empleados_asignados.append(empleado)

    def agregarRegistroTiempo(self, registro: RegistroTiempo) -> None:
        self.__registros_tiempo.append(registro)

    def obtenerTotalHoras(self) -> float:
        return sum(registro.horas for registro in self.__registros_tiempo)

class Empleado:
    def __init__(self, idEmpleado: str, nombre: str, correo: str, salario: float):
        self.__idEmpleado = idEmpleado
        self.__nombre = nombre
        self.__correo = correo
        self.__salario = salario 
        self.__registros_tiempo = [] 
        self.__proyectos = []        
        self.__usuario = None        

    def get_idEmpleado(self) -> str:
        return self.__idEmpleado

    def get_salario(self) -> float:
        return self.__salario
        
    def set_usuario(self, usuario: Usuario) -> None:
        self.__usuario = usuario

    def registrarHoras(self, proyecto: Proyecto, horas: float) -> RegistroTiempo:
        nuevo_registro = RegistroTiempo(f"REG-{len(self.__registros_tiempo)+1}", date.today(), horas)
        
        if nuevo_registro.validarHoras():
            self.__registros_tiempo.append(nuevo_registro)
            proyecto.agregarRegistroTiempo(nuevo_registro)
            return nuevo_registro
        else:
            raise ValueError("Las horas ingresadas no son válidas según las reglas del negocio.")

class Departamento:
    def __init__(self, idDepartamento: str, nombre: str):
        self.__idDepartamento = idDepartamento
        self.__nombre = nombre
        self.__empleados = [] 
        self.__gerente = None 

    def agregarEmpleado(self, e: Empleado) -> None:
        if e not in self.__empleados:
            self.__empleados.append(e)

    def asignarGerente(self, g: Empleado) -> None:
        self.__gerente = g
