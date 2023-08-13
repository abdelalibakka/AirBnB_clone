<<<<<<< HEAD
#!usr/bin/python3

"""Base Class Module"""

import uuid
from datetime import datetime
from copy import deepcopy
import models


class BaseModel():
    """ Base model class """

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance"""

        if len(kwargs.items()) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    self.__setattr__(key,  datetime.fromisoformat(value))
                    continue
                self.__setattr__(key, value)
=======
import uuid
from datetime import datetime

"""module that defines common attr for other classes
"""

class BaseModel:
    """class basemodel"""
    def __init__(self, *args, **kwargs):
        """Initializing class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value,'%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
    
            
            # for key, value in kwargs.items():
            #     if key != '__class__':
            #         setattr(self,key,value)
            # self.id = str(uuid.uuid4())
            # self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            # self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        
>>>>>>> 0c7d4eb90c5b2a86cf17b08b59423df993dc970f
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
<<<<<<< HEAD
            models.storage.new(self)

    def save(self):
        """Update the updated_at attribute with the current datetime"""

        self.updated_at = datetime.now()

        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance
        containing all attributes
        """
        new_dict = deepcopy(self.__dict__)
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """
        Return a string representation of the instance
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
=======

    def __str__(self):
        """string rep of the class"""
        return f'{self.__class__.__name__},{self.id}, {self.__dict__ }'
    
    def save(self):
        """updated instance updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """dict containing key value pairs"""
        n_dict = dict(self.__dict__)
        n_dict['__class__'] = self.__class__.__name__
        for key, value in n_dict.items():
            if isinstance(value, datetime):
                n_dict[key] = value.isoformat()
        # n_dict['created_at'] = n_dict['created_at'].isoformat()
        # n_dict['updated_at'] = n_dict['updated_at'].isoformat()

        return n_dict
>>>>>>> 0c7d4eb90c5b2a86cf17b08b59423df993dc970f
