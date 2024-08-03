from fastapi import APIRouter, status

from DB.Repos import UserRepo
from Schemas.SignUp import SignUpSchema

router = APIRouter(
    tags=["AuthRouter"]
)


@router.post("/sign-up", status_code=status.HTTP_201_CREATED)
async def sign_up(user: SignUpSchema) -> dict:
    await UserRepo.save_user(user)
    return {
        "message": "You have been registered successfully!",
    }
