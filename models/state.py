#!/usr/bin/python3
"""
A module that creates State class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """class State that inherits from BaseModel
    public class attribute:
    name: string - empty string
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Creates a new state
        """
        super().__init__(self, *args, **kwargs)
