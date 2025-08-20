from fastapi import APIRouter, Depends, HTTPException, status,Form,File,UploadFile
import io
from config import supabase
from .utils import current_user
import uuid

router = APIRouter()


@router.post("/send")
async def send_message(msg: str = Form(None), file: UploadFile = File(None), user=Depends(current_user)):
    try:
        user_id = user["sub"]
        image_url = None
        if file:
            print("file",file)
            file_bytes = await file.read()
            unique_name = f"{uuid.uuid4()}-{file.filename}"
            file_path = f"{user_id}/{unique_name}"
            upload_res = supabase.storage.from_("chat-bucket").upload(
                file_path,
                file_bytes,
                {"content-type": file.content_type}
            )
            image_url = supabase.storage.from_("chat-bucket").get_public_url(file_path)
        # Insert user message
        user_msg = supabase.table("messages").insert({
            "user_id": user_id,
            "content": msg,
            "image_url": image_url if image_url else None,
            "role": "user"
        }).execute()

        # Insert assistant response
        assistant_msg = supabase.table("messages").insert({
            "user_id": user_id,
            "content": "This is a response.",
            "role": "assistant"
        }).execute()

        return {
            "user_message": user_msg.data,
            "assistant_message": assistant_msg.data
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
async def get_messages(user=Depends(current_user)):
    try:
        result = supabase.table("messages")\
            .select("*")\
            .eq("user_id", user["id"])\
            .order("created_at", desc=False)\
            .execute()

        return {"messages": result.data}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


