# main.py
from fastapi import FastAPI
from .routes import auth, images, documents  # Importa las rutas que has creado

app = FastAPI()

# Agrega las rutas a la aplicación
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(images.router, prefix="/images", tags=["images"])
app.include_router(documents.router, prefix="/documents", tags=["documents"])

if __name__ == "__main__":
    import uvicorn

    # Inicia la aplicación con uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
