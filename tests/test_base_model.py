#!/usr/bin/python3
"""Module for test BaseModel class"""
import sys
import os
import unittest
import json
import pep8
import datetime
from time import sleep

"""Get the current script's directory
Add the parent directory to the Python path
Get the absolute path of the parent directory (project root)"""
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)


from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Class to test the base model functionality."""
    def test_doc_module(self):
        """module documentation"""
        self.assertGreaterEqual(len(BaseModel.__doc__), 1)

    # def test_pep8_conformance_base_model(self):
    #     """Test that models/base_model.py conforms to PEP8."""
    #     pep8style = pep8.StyleGuide(quiet=True)
    #     result = pep8style.check_files(['models/base_model.py'])
    #     self.assertEqual(result.total_errors, 0,
    #                      "Found code style errors (and warnings).")

    # def test_pep8_conformance_test_base_model(self):
    #     """Test that tests/test_models/test_base_model.py conforms to PEP8."""
    #     pep8style = pep8.StyleGuide(quiet=True)
    #     res = pep8style.check_files(['tests/test_base_model.py'])
    #     self.assertEqual(res.total_errors, 0,
    #                      "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = BaseModel.__init__.__doc__
        self.assertGreaterEqual(len(doc), 1)

    def test_first_task(self):
        """Test creation of class and to_dict"""
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)
        my_model.name = "Edgar"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "Edgar")
        self.assertEqual(my_model.my_number, 89)
        model_types_json = {
            "my_number": int,
            "name": str,
            "__class__": str,
            "updated_at": str,
            "id": str,
            "created_at": str
        }
        my_model_json = my_model.to_dict()
        for key, value in model_types_json.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, my_model_json)
                self.assertIs(type(my_model_json[key]), value)

    def test_base_types(self):
        """Testing dict model"""
        second_model = BaseModel()
        self.assertIs(type(second_model), BaseModel)
        second_model.name = "Andres"
        second_model.my_number = 80
        self.assertEqual(second_model.name, "Andres")
        self.assertEqual(second_model.my_number, 80)
        model_types = {
            "my_number": int,
            "name": str,
            "updated_at": datetime.datetime,
            "id": str,
            "created_at": datetime.datetime
            }
        for key, value in model_types.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, second_model.__dict__)
                self.assertIs(type(second_model.__dict__[key]), value)

    def test_uuid(self):
        """testing differents uuid"""
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_datetime_model(self):
        """testing datetime base model"""
        model_x = BaseModel()
        model_y = BaseModel()
        self.assertNotEqual(model_x.created_at, model_x.updated_at)
        self.assertNotEqual(model_x.created_at, model_y.created_at)

    def test_string_representation(self):
        """Test the magic method str"""
        my_model = BaseModel()
        my_model.name = "Edgar"
        my_model.my_number = 89
        id_model = my_model.id

        expected = 'BaseModel,{}, {}'\
                   .format(id_model, my_model.__dict__)
        self.assertEqual(str(my_model), expected)

    def test_constructor_kwargs(self):
        """Test constructor that has kwargs as attributes values"""
        obj = BaseModel()
        obj.name = "Edgar"
        obj.my_number = 89
        json_attributes = obj.to_dict()

        obj2 = BaseModel(**json_attributes)

        self.assertIsInstance(obj2, BaseModel)
        self.assertIsInstance(json_attributes, dict)
        self.assertIsNot(obj, obj2)
        self.assertEqual(obj.to_dict(), obj2.to_dict())

    def test_file_save(self):
        """Test that info is saved to file"""
        b3 = BaseModel()
        b3.save()
        with open("file.json", 'r') as f:
            self.assertIn(b3.id, f.read())
        

if __name__ == '__main__':
    unittest.main()

