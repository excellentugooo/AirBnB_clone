#!/usr/bin/python3
"""
This File defines the BaseModel class that will
serve as the base class for all our models."""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all our classes"""

    def __init__(self, *args, **kwargs):
        """constructor it either deserialize
        a serialized class or initialize a new"""

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """override str representation of self"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates last updated variable"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of self"""
        dict_dup = self.__dict__.copy()
        dict_dup["__class__"] = self.__class__.__name__
        dict_dup["created_at"] = self.created_at.isoformat()
        dict_dup["updated_at"] = self.updated_at.isoformat()
        return dict_dup
