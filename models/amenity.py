#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy import Table


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = realationship("place", secondary='place_amenity')
