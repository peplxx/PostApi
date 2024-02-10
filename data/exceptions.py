from fastapi import HTTPException
from fastapi import status

PostNotExist = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post with such id doesn't exist!")