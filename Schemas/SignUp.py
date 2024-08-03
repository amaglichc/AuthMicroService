from pydantic import BaseModel, EmailStr


class SignUpSchema(BaseModel):
    username: str
    password: str
    email: EmailStr
