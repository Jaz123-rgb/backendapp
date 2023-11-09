from pydantic import BaseModel
from app.authentication.security import get_password_hash

class User(BaseModel):
    username: str
    password: str
    email: str
    roles: list[str] = []

    @classmethod
    def create_user(cls, username: str, password: str, email: str, roles: list[str] = None):
        # Encripta la contraseña antes de almacenarla en la base de datos
        password_hash = get_password_hash(password)
        return cls(username=username, password=password_hash, email=email, roles=roles)

# Agregar usuarios de prueba
users = [
    User.create_user(username="jaz", password="1234", email="jaziellpv@gmail.com"),
    # Agrega más usuarios si es necesario
]
 