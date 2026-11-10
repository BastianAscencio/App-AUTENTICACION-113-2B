#Genera los hash
import hashlib
#Genera el Salt
import secrets
#Realiaza la comparacion de contraseñas
import hmac

#Crear tipo de clase
class Usuario:

    ITERACIONES = 600_000
    #Constructor def
    def _init_(self, nombre, correo, password):
        self.nombre = nombre 
        self.correo = correo
        self._salt = secrets.token_bytes(16)
        self._password_hash = self.generar_hash(password)

    def generar_hash(self, password):

     #la contraseña se convierte a bytes antes del calculo
        password_bytes = password.encode("utf-8")

        return hashlib.pbkdf2_hmac(            
            "sha256",
            password_bytes,
            self._salt,
            self.ITERACIONES
        )

    def verificar_password(self, password):

        nurvo_hash = self.generar_hash(password)

        return hmac.compare_digest(
            self._password_hash,
            nuevo_hash 
        )

    def cambiar_password(self, nuevo_password):

        self._salt = secrets.token_bytes(16)
        self._password_hash = self.generar_hash(nueva_password)

    def mostrar_datos(self):
        print("\n  --Datos del Usuario--")
        print("Nombre: ", self.nombre)
        print("Correo: ", self.correo)
        print("Contraseña: **********" )