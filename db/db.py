from motor.motor_asyncio import AsyncIOMotorClient

# URL de conexión a tu base de datos MongoDB
mongo_url = "mongodb://localhost:27017"  # Reemplaza con la URL de tu base de datos

# Conexión a la base de datos
client = AsyncIOMotorClient(mongo_url)
db = client["managebase"]  # Reemplaza "your_database_name" con el nombre de tu base de datos
documents_collection = db["managebaseone"]  # Agrega esta línea para especificar la colección
