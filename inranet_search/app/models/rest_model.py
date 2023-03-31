from pydantic import BaseModel


class ProcessFileRequest(BaseModel):
    external_id: int
    file_name: str
    file_content_type: str
    file_content: bytes
