#!/usr/bin/python3
"""
Initialize FileStorage and reload data from the JSON file into the storage.
"""

# Import the FileStorage class from the models.engine module
from models.engine import file_storage

# Create an instance of FileStorage
storage = file_storage.FileStorage()

# Reload data from the JSON file into the storage
storage.reload()
