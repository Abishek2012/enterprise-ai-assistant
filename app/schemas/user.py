from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

from app.models.role import UserRole


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)