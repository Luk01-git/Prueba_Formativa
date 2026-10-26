import sqlite3

class DatabaseManager:
    def __init__(self, db_name="ecotech_solutions.db"):
        self.db_name = db_name
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = sqlite3.connect(self.db_name)
            return self.conexion
        except sqlite3.Error as e:
            print(f"[BD] Error al conectar a la base de datos: {e}")
            return None

    def crear_tablas_iniciales(self):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Empleado (
                    idEmpleado TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    correo TEXT NOT NULL,
                    salario REAL NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Usuario (
                    idUsuario TEXT PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    contrasenaHash TEXT NOT NULL,
                    idEmpleado TEXT,
                    FOREIGN KEY(idEmpleado) REFERENCES Empleado(idEmpleado)
                )
            ''')
            self.conexion.commit()

    def registrar_empleado_y_usuario(self, id_emp, nombre, correo, salario, id_usr, username, contrasena_hash):
        if self.conexion:
            cursor = self.conexion.cursor()
            try:
                cursor.execute('INSERT INTO Empleado VALUES (?, ?, ?, ?)', 
                               (id_emp, nombre, correo, salario))
                cursor.execute('INSERT INTO Usuario VALUES (?, ?, ?, ?)', 
                               (id_usr, username, contrasena_hash, id_emp))
                
                self.conexion.commit()
                return True
            except sqlite3.IntegrityError:
                return False 

    def obtener_datos_login(self, username):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('''
                SELECT u.contrasenaHash, e.idEmpleado, e.nombre, e.correo, e.salario 
                FROM Usuario u
                JOIN Empleado e ON u.idEmpleado = e.idEmpleado
                WHERE u.username = ?
            ''', (username,))
            return cursor.fetchone()
        return None

    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()
