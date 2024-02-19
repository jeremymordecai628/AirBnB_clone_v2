#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
import sys
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey



class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    if models.storage_type == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
