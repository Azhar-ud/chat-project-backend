from fastapi import HTTPException,status,Depends,APIRouter
from config import supabase
from .schemas import Signup

router = APIRouter()

@router.post("/signup")
def signup(data: Signup):
    try:
        result = supabase.auth.sign_up({"email":data.email,"password": data.password, })
        return result
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/login")
async def login(data:Signup):
    try:
        result = supabase.auth.sign_in_with_password({"email":data.email,"password": data.password})
        return {"access_token": result.session.access_token, "email": result.user.email}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))




