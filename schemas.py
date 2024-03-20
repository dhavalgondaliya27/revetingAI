from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str
    
# class TeamCreate(BaseModel):
#     team_name: str
#     user_email: list

class CommentCreate(BaseModel):
    text: str


