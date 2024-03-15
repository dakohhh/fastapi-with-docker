from fastapi import APIRouter, Request, status
from authentication.auth import Auth
from database.schema import User
from client.response import CustomResponse
from utils.query import LoginSchema


router = APIRouter(tags=["Auth"], prefix="/auth")



auth = Auth()


@router.post("/login")
async def login_student(request: Request, login_input: LoginSchema):

    token = await auth.authenticate_user(login_input)

    context = {"token": token}

    return CustomResponse("login user successfully", data=context)




