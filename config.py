import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

supabase:Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_supabase_user_client(user_token:str) -> Client:
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY, headers={"Authorization": f"Bearer {user_token}"})