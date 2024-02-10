from pydantic import BaseModel


class PostData(BaseModel):
    title: str
    content: str
    published: bool = True