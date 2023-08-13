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
    """
    public instance method that returns the
    dictionary __objects.
    """
    __file_path: str = 'file.json'
    __objects: dict = {}

    def all(self):
        """
        public instance method that returns the
        dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        public instance method that sets in __objects
        the obj with key <obj class name>.id
        Variables:
        ----------
        key [str] -- key format generated.
        """
        if obj:
            key = f'{obj.__class__.__name__}.{obj.id}'
            self.__objects[key] = obj

    def save(self):
        """
        public instance method that serializes __objects
        to the JSON file (path: __file_path).
        Variables:
        ----------
        new_dict [dict] -- keys and values to build JSON.
        """
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict().copy()
        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        public instance method that deserializes a JSON
        file to __objects.
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
            for v in data.values():
                class_name = v['__class__']
                if isinstance(class_name, str) and type(eval(class_name)) == type:
                    self.new(eval(class_name)(**v))
        except FileNotFoundError:
            pass

