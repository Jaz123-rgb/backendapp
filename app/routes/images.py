# routes/images.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from ..authentication.authentication import get_current_user

router = APIRouter()

@router.get("/")
async def list_images(current_user: dict = Depends(get_current_user)):
    # Aquí deberías obtener y devolver la lista de imágenes según el rol del usuario
    # Ejemplo básico:
    if current_user["role"] == "admin" or current_user["role"] == "uploader":
        # Lógica para obtener la lista de imágenes (simulación)
        images_list = ["image1.jpg", "image2.png"]
        return {"images": images_list}
    else:
        raise HTTPException(
            status_code=403,
            detail="Permission denied. You do not have the necessary role.",
        )

@router.post("/")
async def upload_image(current_user: dict = Depends(get_current_user)):
    # Aquí deberías implementar la lógica para cargar una imagen según el rol del usuario
    # Ejemplo básico:
    if current_user["role"] == "admin" or current_user["role"] == "uploader":
        # Lógica para cargar la imagen (simulación)
        return JSONResponse(content={"message": "Image uploaded successfully"}, status_code=201)
    else:
        raise HTTPException(
            status_code=403,
            detail="Permission denied. You do not have the necessary role.",
        )

@router.delete("/{image_id}")
async def delete_image(image_id: int, current_user: dict = Depends(get_current_user)):
    # Aquí deberías implementar la lógica para eliminar una imagen según el rol del usuario
    # Ejemplo básico:
    if current_user["role"] == "admin":
        # Lógica para eliminar la imagen (simulación)
        return JSONResponse(content={"message": f"Image {image_id} deleted successfully"}, status_code=200)
    else:
        raise HTTPException(
            status_code=403,
            detail="Permission denied. You do not have the necessary role.",
        )
