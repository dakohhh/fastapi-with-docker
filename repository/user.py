from database.schema import User
from authentication.hashing import hashPassword
from utils.query import SignupSchema
import typing


class UserRepository:

    @staticmethod
    async def create_user(signup_input: SignupSchema) -> User:

        query = User(
            firstname=signup_input.firstname,
            lastname=signup_input.lastname,
            password=hashPassword(signup_input.password),
            email=signup_input.email,
        )

        query.save()

        return query

    @staticmethod
    async def does_user_email_exits(email: str) -> bool:

        query = User.objects(email=email).first()

        return query is not None

    @staticmethod
    async def get_user_by_email(email: str) -> typing.Union[User, None]:

        query = User.objects(email=email).first()

        return query

    @staticmethod
    async def get_user_by_id(User_id: str) -> typing.Union[User, None]:

        query = User.objects(id=User_id).first()

        return query
