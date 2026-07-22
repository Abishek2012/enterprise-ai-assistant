from fastapi import HTTPException, status


class ChatService:

    def get_response(self, message: str) -> str:

        message = message.strip()

        if not message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Message cannot be empty."
            )

        return f"You said: {message}"


chat_service = ChatService()