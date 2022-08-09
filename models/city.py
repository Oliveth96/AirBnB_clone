#!/usr/bin/python3
"""
A module that creates city class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel
    public class attributes:
    state_id: string - empty string
    name: string - empty string
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates a new city
        """
        super().__init__(self, *args, **kwargs)
