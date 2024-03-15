from mongoengine import (
    Document,
    StringField,
    EmailField,
    DateTimeField,
    URLField,
    ReferenceField,
    BooleanField,
)
from datetime import datetime


class User(Document):

    firstname = StringField(required=True, min_lenght=3, max_length=50)

    lastname = StringField(required=True, min_lenght=3, max_length=50)

    email = EmailField(required=True, unique=True)

    password = StringField(required=True)

    created_at = DateTimeField(default=datetime.now())

    updated_at = DateTimeField(default=datetime.now())

    meta = {"strict": False}

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
        }
