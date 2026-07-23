from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.role import UserRole
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password


class UserService:

    @staticmethod
    def create_user(db: Session, user: UserCreate) -> User:
        existing_user = (
            db.query(User)
            .filter(User.email == user.email)
            .first()
        )

        if existing_user:
            raise HTTPException(
                status_code=409,
                detail="Email already registered"
            )

        new_user = User(
            name=user.name,
            email=user.email,
            password=hash_password(user.password),
            role=UserRole.USER
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def get_all_users(db: Session):
        return db.query(User).all()

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )