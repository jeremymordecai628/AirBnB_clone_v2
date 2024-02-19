#!/usr/bin/python3
"""This represents the file storage class utilized by AirBnB."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and deserializes a JSON file to instances. It possesses the following attributes:

__file_path: the path to the JSON file
__objects: storage for objects
    """
    __file_path = "file.json"
    __objects = {}

    def delete(self, obj=None):
        """deletes obj from __objects if it's inside
        Args:
            obj: given object
        """
        if obj is None:
            return
        key = "{}.{}".format(type(obj).__class__.__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]
            self.save()

    def all(self, cls=None):
        """returns a dictionary
        Args:
            cls: class type to filter return by
        Return:
            returns a dictionary of __object
        """
        if not cls:
            return self.__objects
        return {k: v for k, v in self.__objects.items() if type(v) == cls}

    def new(self, obj):
        """Assigns the given object to the __objects attribute.

Parameters:
- obj: the given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Converts the file path to a JSON file path in a serialized format.
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Converts the file path to a JSON file path in a serialized format.
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """Reloads to deserialize objects from a JSON file."""
        self.reload()
