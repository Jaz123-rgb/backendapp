# main.py
from fastapi import FastAPI
from app.routes import auth  # Importa las rutas que has creado

app = FastAPI()

# Agrega las rutas a la aplicación
app.include_router(auth.router)

if __name__ == "__main__":
    import uvicorn

    # Inicia la aplicación con uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
