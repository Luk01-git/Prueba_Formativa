import sqlite3
from datetime import date
import hashlib

class DatabaseManager:
    """Gestiona la persistencia utilizando la librería oficial sqlite3."""
    def __init__(self, db_name="ecotech_solutions.db"):
        self.db_name = db_name
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = sqlite3.connect(self.db_name)
            print(f"[BD] Prueba de conexión exitosa a la base de datos: {self.db_name}")
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
            self.conexion.commit()
            print("[BD] Estructura de tablas inicializada correctamente.")

    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()
            print("[BD] Conexión cerrada.")
