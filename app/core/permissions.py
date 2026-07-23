from fastapi import Depends, HTTPException, status

from app.core.dependencies import get_current_user
from app.models.role import UserRole
from app.models.user import User


def admin_required(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Allow access only to administrators.
    """

    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action."
        )

    return current_user