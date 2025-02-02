#!/usr/bin/python3
"""Base Model (Parent class)"""

import uuid
from models import dataStorage
from datetime import datetime


class BaseModel:

    """Parent Class which all other classes will inherit from"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes like id: uuid,
        and dates when created and updated

        Args:
            - *args: list of arguments
            - **kwargs: key-values pair arguments
        """

        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], date_format)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], date_format)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            dataStorage.new(self)

    def __str__(self):
        """Returns string representation of instance, arguments, date and id"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Method to update the date of the public instance attribute
        updated_at
        """

        self.updated_at = datetime.now()
        dataStorage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values pairs of __dict_
        and date in string format
        """

        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
