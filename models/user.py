#!/usr/bin/python3

"""This file defines the UserModel class
It inherits from the BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """The User Model"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
