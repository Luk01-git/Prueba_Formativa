import hashlib

class Usuario:
    """Clase encargada de autenticar usuarios y proteger credenciales."""
    def __init__(self, idUsuario: str, username: str, contrasena: str):
        self.__idUsuario = idUsuario
        self.__username = username
        # Cifrado con algoritmo SHA-256 (hashlib) según requerimientos de seguridad.
        self.__contrasenaHash = hashlib.sha256(contrasena.encode()).hexdigest()

    def autenticar(self, password_intento: str) -> bool:
        """Autentica comparando el hash de la contraseña."""
        hash_intento = hashlib.sha256(password_intento.encode()).hexdigest()
        return self.__contrasenaHash == hash_intento

    def validarAcceso(self, rol: str) -> bool:
        return True # Lógica a expandir según roles de negocio
