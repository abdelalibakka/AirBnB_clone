#!/usr/bin/python3
"""This module_has the_review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Implementation_of review_class"""

    place_id = ""
    user_id = ""
    text = ""
