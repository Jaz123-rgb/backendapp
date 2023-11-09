from pydantic import BaseModel
from app.authentication.security import get_password_hash
from motor.motor_asyncio import AsyncIOMotorClient

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



async def create_user(username: str, password: str, email: str, roles: list[str] = None):
    password_hash = get_password_hash(password)
    user_data = {
        "username": username,
        "password": password_hash,
        "email": email,
        "roles": roles if roles else [],
    }

    # Conecta a la base de datos MongoDB
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["mydatabase"]
    users_collection = db["users"]

    # Inserta el usuario en la colección de usuarios
    result = await users_collection.insert_one(user_data)

    # Devuelve el ID del usuario insertado
    return str(result.inserted_id)
