#!/usr/bin/python3
"""Persistent storage"""

from models.base_model import BaseModel
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}

class FileStorage:
    """File-based persistent storage."""
    __file_path: str = 'file.json'
    __objects: dict = {}

    def all(self):
        """returns dictionary objs"""
        return self.__objects

    def new(self, obj):
        """sets obj with key as <obj class name>.id"""
        if obj:
            key = f'{obj.__class__.__name__}.{obj.id}'
            self.__objects[key] = obj

    def save(self):
        """saves objects to file in json format"""
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict().copy()
        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """deserialize json file only if __file_path exists"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
            for v in data.values():
                if isinstance(class_name, str) and type(eval(class_name)) == type:
                    self.new(eval(class_name)(**v))
        except FileNotFoundError:
            pass

