# -*- coding: utf-8 -*-
"""Lot model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Text
from sqlalchemy.orm import relationship, backref

from central.model import DeclarativeBase, metadata, DBSession


class Lot(DeclarativeBase):
    __tablename__ = 'lots'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    cars = Column(Integer, default=int)

    nodes = relationship('Node', back_populates='lot')

__all__ = ['Lot']
