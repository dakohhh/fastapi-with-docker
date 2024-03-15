import asyncio
from beanie import PydanticObjectId
from pydantic import EmailStr
from fastapi import APIRouter, Depends, Request, BackgroundTasks, status
from authentication.auth import Auth
from authentication.hashing import checkPassword, hashPassword
from client.response import CustomResponse
from database.schema import User
from repository import UserRepository
from utils.query import SignupSchema
from exceptions.custom_exception import BadRequestException


router = APIRouter(tags=["User"], prefix="/user")


auth = Auth()


@router.post("/signup")
async def signup_student(request: Request, signup_input: SignupSchema):

    user = await UserRepository.does_user_email_exits(signup_input.email)

    if user:
        raise BadRequestException("this email already exists")
    
    user = await UserRepository.create_user(signup_input)

    context = {"user": user.to_dict()}

    return CustomResponse(
        "signup user successfully", data=context, status=status.HTTP_201_CREATED
    )





@router.get("/")
async def get_logged_in_user(request: Request, user:User=Depends(auth.get_current_user)):

    context = {"user": user.to_dict()}

    return CustomResponse(
        "get logged in user", data=context, status=status.HTTP_201_CREATED
    )


