"""
The `Models.py` file is where all models are held.

This may be changed in the future so models are
contained in their own file and or directory,
but as of now, they must be in Models.py.
"""

import datetime
from Config.Environment import env, get_database
from peewee import *

db = get_database(env("DB_TYPE"))


class BaseModel(Model):
    class Meta:
        database = db


# Write your database models here! Remember to
# inherit from BaseModel!
