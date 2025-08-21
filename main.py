from fastapi import FastAPI
from auth import routes as auth_routes
from fastapi.middleware.cors import CORSMiddleware
from auth import chat as messages_routes


app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
    "https://chat-project-frontend-blush.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # No "*" if allow_credentials=True
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(messages_routes.router, prefix="/chat", tags=["Chat"])

@app.get("/")
def root():
    return {"message": "Hello from main.py"}


