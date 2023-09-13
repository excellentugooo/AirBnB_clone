#!/usr/bin/python3
"""
This File defines the storage system (File System)
For the project.
It uses json format to serialize or deserialize
an object"""

import json
from models.base_model import BaseModel


class FileStorage():
    """This class serve as an ORM to interface between or Storage System"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all instances stored"""
        return self.__objects

    def new(self, obj):
        """Stores a new Object"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes objects stored and persist in file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """de-serialize persisted objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                desrialize = json.load(f)
                for i in desrialize.values():
                    cls = i["__class__"]
                    del o["__class__"]
                    self.new(eval(cls)(**i))

        except (FileNotFoundError):
            return
