#!/usr/bin/python3
"""
this_module holds_class FileStorage
"""

import json
from models.base_model import BaseModel
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
    """
    Implementation_of the_class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the_dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects_the obj with_key <obj class name>.id
        """
        if not obj:
            return
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to_the JSON_file (path: __file_path)
        """
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_obj, f)

    def reload(self):
        """
        Deserializes_the JSON_file to __objects (only if the JSON
        file (__file_path) exists
        """
        try:
            with open(self.__file_path, 'r') as f:
                j_obj = json.load(f)
            for k in j_obj:
                self.__objects[k] = classes[j_obj[k]["__class__"]](**j_obj[k])
        except Exception:
            pass
