#!/usr/bin/python3
"""Module for test BaseModel class"""
import unittest
import json
# import pep8
import datetime
from time import sleep

import sys
import os

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path of the parent directory (project root)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))

# Add the parent directory to the Python path
sys.path.insert(0, parent_dir)

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Class to test the base model functionality."""
    def test_doc_module(self):
        """module documentation"""
        self.assertGreaterEqual(len(BaseModel.__doc__), 1)

if __name__ == '__main__':
    unittest.main()

