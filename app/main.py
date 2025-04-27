from fastapi import FastAPI
from auth import router as auth_router

app = FastAPI()

# Include the auth router for registration/login
app.include_router(auth_router, prefix="/auth")