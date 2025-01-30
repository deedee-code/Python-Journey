from pydantic import BaseModel, Field

class CreateUserDTO(BaseModel):  
    name: str = Field(min_length=3, title="User name")
    gender: str = Field(min_length=3, title="User gender")
    age: int = Field
    
class UpdateUserInfoDto(BaseModel):  
    name: str = Field(min_length=3, title="User name")
    gender: str = Field(min_length=3, title="User gender")
    age: int = Field
