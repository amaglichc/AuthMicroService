from fastapi import FastAPI
from Roouters.AuthRouter import router as AuthRouter
app = FastAPI(
    title="AuthService"
)

app.include_router(AuthRouter)