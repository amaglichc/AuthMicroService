import uuid

from sqlalchemy.orm import Mapped, mapped_column
from DB.core import Base


class UserOrm(Base):
    __tablename__ = 'user'
    id: Mapped[str] = mapped_column(primary_key=True,default=str(uuid.uuid4()))
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
