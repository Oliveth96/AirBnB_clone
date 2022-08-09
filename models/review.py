#!/usr/bin/python3
"""
A module that creates review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel
    Public class attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Creates a new review
        """
        super().__init__(self, *args, **kwargs)
