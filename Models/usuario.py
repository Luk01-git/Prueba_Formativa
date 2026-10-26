import hashlib

class Usuario:
    def __init__(self, idUsuario: str, username: str, contrasena: str, is_hashed: bool = False):
        self.__idUsuario = idUsuario
        self.__username = username
        
        if is_hashed:
            self.__contrasenaHash = contrasena
        else:
            self.__contrasenaHash = hashlib.sha256(contrasena.encode()).hexdigest()

    def get_hash(self) -> str:
        return self.__contrasenaHash

    def autenticar(self, password_intento: str) -> bool:
        hash_intento = hashlib.sha256(password_intento.encode()).hexdigest()
        return self.__contrasenaHash == hash_intento

    def validarAcceso(self, rol: str) -> bool:
        return True
