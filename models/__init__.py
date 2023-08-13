#!/usr/bin/python3
""" initiate FileStoarge """
from models.engine.file_storage import FileStorage

"""instance of storage"""
storage = FileStorage()
storage.reload()
