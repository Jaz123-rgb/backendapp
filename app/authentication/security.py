# authentication/security.py

from passlib.context import CryptContext
from app.models import User
from app.authentication.password_utils import get_password_hash  # Importa la función get_password_hash desde hashing.py

# Crea una instancia de la clase CryptContext para manejar contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    # Buscar el usuario en la base de datos por su nombre de usuario
    user = get_user_from_db(username)
    if user is None:
        return None

    # Verificar la contraseña
    if not verify_password(password, user.password):
        return None

    return user

def get_user_from_db(username: str):
    # Implementa la lógica para buscar y devolver el usuario de la base de datos
    # Puedes usar tu propio método para acceder a la base de datos aquí

    # Ejemplo de cómo podrías buscar un usuario en una lista de usuarios
    # Esto debe adaptarse a tu implementación real de la base de datos
    users = [
        User(username="user1", password=get_password_hash("password1")),
        User(username="user2", password=get_password_hash("password2")),
    ]

    for user in users:
        if user.username == username:
            return user

    return None
