# auth/seguridad.py
import os
import hashlib
import binascii
import time
from persistence.datos import RepositorioDatos

REINTENTOS_LOG = "auth_attempts.log"

class AuthError(Exception):
    pass

class AuthService:
    def __init__(self, repo: RepositorioDatos):
        self.repo = repo
        self.current_user = None

    # --- Generar hash seguro ---
    def _generar_salt(self, length=16):
        return binascii.hexlify(os.urandom(length)).decode()

    def _hash_password(self, password, salt, iterations=100000):
        pwd = password.encode("utf-8")
        salt_bytes = salt.encode("utf-8")
        dk = hashlib.pbkdf2_hmac("sha256", pwd, salt_bytes, iterations)
        return binascii.hexlify(dk).decode()

    # --- Registro de usuario ---
    def registrar_usuario(self, username, password, rol="user"):
        if self.repo.buscar_usuario(username):
            raise AuthError("Usuario ya existe.")
        salt = self._generar_salt()
        pwd_hash = self._hash_password(password, salt)
        user = {"username": username, "password_hash": pwd_hash, "salt": salt, "rol": rol}
        self.repo.guardar_usuario(user)
        print(f"✅ Usuario '{username}' registrado con rol '{rol}'.")

    # --- Login ---
    def login(self, username, password):
        user = self.repo.buscar_usuario(username)
        if not user:
            self._registrar_intento(username, success=False, reason="no_exist")
            return False
        calc_hash = self._hash_password(password, user["salt"])
        if calc_hash == user["password_hash"]:
            self.current_user = {"username": username, "rol": user["rol"]}
            self._registrar_intento(username, success=True)
            return True
        else:
            self._registrar_intento(username, success=False, reason="bad_password")
            return False

    def logout(self):
        self.current_user = None

    # --- Verificación de rol ---
    def require_role(self, rol):
        return self.current_user and self.current_user["rol"] == rol

    # --- Registro de intentos ---
    def _registrar_intento(self, username, success, reason=""):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        linea = f"{timestamp} | user:{username} | success:{success} | reason:{reason}\n"
        with open(REINTENTOS_LOG, "a", encoding="utf-8") as f:
            f.write(linea)