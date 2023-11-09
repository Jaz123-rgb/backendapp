# hashing.py

from passlib.context import CryptContext

# Crea una instancia de la clase CryptContext para manejar contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)
