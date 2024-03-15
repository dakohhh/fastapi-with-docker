from typing import List, Optional
from fastapi import Form, UploadFile, File
from pydantic import BaseModel, EmailStr, HttpUrl
from beanie import PydanticObjectId
from datetime import datetime


class LoginSchema(BaseModel):

    email: EmailStr

    password: str


class SignupSchema(BaseModel):

    firstname: str

    lastname: str

    password: str

    email: EmailStr




class Token(BaseModel):
    user: str
    exp: int

    def get_expiry_time(self):
        return datetime.utcfromtimestamp(self.exp)
