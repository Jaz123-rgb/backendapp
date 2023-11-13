# routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.authentication import authentication

router = APIRouter()

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Aquí deberías validar las credenciales del usuario, por ejemplo, con una consulta a la base de datos.
    # Si las credenciales son válidas, crea y devuelve un token JWT.
    # De lo contrario, lanza una excepción HTTPException con código 401.
    # Puedes usar la función create_jwt_token del módulo jwt.py para crear el token.
    # El token se devolverá al cliente y se usará en las solicitudes subsiguientes.

    # Ejemplo básico (necesitas ajustarlo según tu lógica de autenticación):
    fake_user = {"username": form_data.username, "password": form_data.password}
    if fake_user["password"] != "password123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    token = authentication.create_jwt_token(data={"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}
