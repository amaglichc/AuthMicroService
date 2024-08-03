from DB.Orms.UserOrm import UserOrm
from DB.core import session_factory
from Schemas.SignUp import SignUpSchema
from passlib.hash import pbkdf2_sha256

async def save_user(user: SignUpSchema):
    async with session_factory.begin() as session:
        hash_password = pbkdf2_sha256.hash(user.password)
        user_orm: UserOrm = UserOrm(username=user.username,email=user.email,password=hash_password)
        session.add(user_orm)
        await session.commit()

