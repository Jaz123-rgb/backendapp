from fastapi import FastAPI
from bson import ObjectId
from db.db import documents_collection
from app.routes import auth
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.authentication.security import authenticate_user, create_access_token
from db.db import documents_collection
from app.models import User
import asyncio

app = FastAPI()

# Ruta de ejemplo
@app.get("/")
async def read_root():
    return {"message": "¡Bienvenido a tu API con FastAPI!"}

app.include_router(auth.router, prefix="/auth", tags=["tags"])

# Ruta para obtener todos los documentos desde la base de datos MongoDB
@app.get("/documents/")
async def get_documents():
    documents = await documents_collection.find({}).to_list(None)
    documents = [str(doc["_id"]) for doc in documents]
    return documents

# Ruta para agregar un nuevo documento a la base de datos
@app.post("/documentspost/")
async def create_document(document_data: dict):
    result = await documents_collection.insert_one(document_data)
    return {"message": "Documento creado con éxito", "inserted_id": str(result.inserted_id)}

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Función para crear el usuario al inicio del servidor
async def create_initial_user():
    # Verificar si el usuario ya existe en la base de datos
    existing_user = await documents_collection.find_one({"username": "jaz"})

    if existing_user is None:
        # El usuario no existe, así que lo creamos
        new_user = User.create_user(username="jaz", password="1234", email="jaziellpv@gmail.com")
        # Insertamos el nuevo usuario en la base de datos
        await documents_collection.insert_one(new_user.dict())

if __name__ == "__main__":
    import uvicorn
    from app.authentication.security import get_password_hash

    # Crear el usuario al iniciar el servidor
    asyncio.run(create_initial_user())

    uvicorn.run(app, host="0.0.0.0", port=8000)
