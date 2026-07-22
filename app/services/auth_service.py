from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.models.user import User
from app.schemas.auth import LoginRequest, Token
from app.utils.security import verify_password


class AuthService:

    @staticmethod
    def login(db: Session, login_data: LoginRequest) -> Token:
        user = (
            db.query(User)
            .filter(User.email == login_data.email)
            .first()
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if not verify_password(login_data.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        access_token = create_access_token(
            data={"sub": user.email}
        )

        return Token(
            access_token=access_token,
            token_type="bearer"
        )