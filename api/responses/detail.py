from pydantic import BaseModel


class DetailResponse(BaseModel):
    """
    DetailResponse model
    """

    message: str
