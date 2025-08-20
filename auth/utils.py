from fastapi import HTTPException,Depends,status
from fastapi.security import HTTPBearer
from config import supabase


security = HTTPBearer()

def current_user(credentials=Depends(security)):
    token = credentials.credentials
    print(token)
    response = supabase.auth.get_user(token)
    print(response)
    try:
        # Verify token with the admin client
        response = supabase.auth.get_user(token)
        print(response)
        
        if not response.user:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        return {
            "id": response.user.id,
            "email": response.user.email,
            "access_token": token,
            "sub": response.user.id
        }
    except Exception:
        raise HTTPException(status_code=401, detail="Could not validate credentials")