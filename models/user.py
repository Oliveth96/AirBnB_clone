#!/usr/bin/python3
"""
A module that creates user class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """A class User that inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Creates a new user
        """
        super().__init__(self, *args, **kwargs)
