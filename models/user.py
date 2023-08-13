#!/usr/bin/python3
"""Module that define the user class"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """User class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
