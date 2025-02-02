#!/usr/bin/python3
"""Module for Airbnb Clone FileStorage class"""

import os
import json

class FileStorage:
    """Class for storing and retrieving data
    Class Methods:
        all: Returns the object (dictionary object)
        new: updates the object id
        save: Converts Python objects into JSON strings
        reload: Converts JSON strings into Python objects
    Class Attributes:
        __file_path (str): The name of the file objects are saved to
        __objects (dict): A dictionary of instantiated objects
        class_dict (dict): A dictionary of all the classes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects: object instance"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Converts __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """Returns classes and their respective refs"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
                   "Place": Place, "Review": Review, "State": State, "User": User}
        return classes

    def reload(self):
        """Reloads objects if exists and stored"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {key: self.classes()[value["__class__"]](**value)
            for key, value in obj_dict.items()}
            FileStorage.__objects = obj_dict
