from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel  # Importa el modelo User
from app.authentication.security import authenticate_user, create_access_token

# Define un modelo Pydantic para la solicitud de inicio de sesión
class LoginRequest(BaseModel):
    username: str
    password: str

