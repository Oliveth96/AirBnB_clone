#!/usr/bin/python3
"""
A module that creates amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """The class Amenity that inherits from BaseModel
    public class attribute:
    name: string - empty string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """create new amenity
        """
        super().__init__(self, *args, **kwargs)
