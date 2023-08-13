#!/usr/bin/python3
"""module that defines common attr for other classes
"""

import uuid
from datetime import datetime
import models

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
        
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string rep of the class"""
        return f'{self.__class__.__name__},{self.id}, {self.__dict__ }'
    
    def save(self):
        """updated instance updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

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
    
