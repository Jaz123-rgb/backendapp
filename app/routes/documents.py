# routes/documents.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from ..authentication.authentication import get_current_user

router = APIRouter()

@router.get("/")
async def list_documents(current_user: dict = Depends(get_current_user)):
    # Aquí deberías obtener y devolver la lista de documentos según el rol del usuario
    # Ejemplo básico:
    if current_user["role"] == "admin" or current_user["role"] == "uploader":
        # Lógica para obtener la lista de documentos (simulación)
        documents_list = ["document1.pdf", "document2.doc"]
        return {"documents": documents_list}
    else:
        raise HTTPException(
            status_code=403,
            detail="Permission denied. You do not have the necessary role.",
        )

@router.post("/")
async def upload_document(current_user: dict = Depends(get_current_user)):
    # Aquí deberías implementar la lógica para cargar un documento según el rol del usuario
    # Ejemplo básico:
    if current_user["role"] == "admin" or current_user["role"] == "uploader":
        # Lógica para cargar el documento (simulación)
        return JSONResponse(content={"message": "Document uploaded successfully"}, status_code=201)
    else:
        raise HTTPException(
            status_code=403,
            detail="Permission denied. You do not have the necessary role.",
        )

@router.delete("/{document_id}")
async def delete_document(document_id: int, current_user: dict = Depends(get_current_user)):
    # Aquí deberías implementar la lógica para eliminar un documento según el rol del usuario
    # Ejemplo básico:
    if current_user["role"] == "admin":
        # Lógica para eliminar el documento (simulación)
        return JSONResponse(content={"message": f"Document {document_id} deleted successfully"}, status_code=200)
    else:
        raise HTTPException(
            status_code=403,
            detail="Permission denied. You do not have the necessary role.",
        )
