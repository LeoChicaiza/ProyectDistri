from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.users_me import router as me_router

app = FastAPI()

app.include_router(auth_router)  # El prefix ya va en el router
app.include_router(me_router, prefix="/users")

@app.get("/health", tags=["health"])
async def health():
    return {"status": "ok"}
