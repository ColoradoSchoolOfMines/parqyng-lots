# -*- coding: utf-8 -*-
"""Lot model module."""
from sqlalchemy import *
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import backref, relationship
from sqlalchemy.types import Integer, Text

from central.model import DBSession, DeclarativeBase, metadata


class Lot(DeclarativeBase):
    __tablename__ = 'lots'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    cars = Column(Integer, default=int)
    capacity = Column(Integer, default=int)

    nodes = relationship('Node', back_populates='lot')

    @property
    def status(self):
        if self.cars < 0.9 * self.capacity:
            return 'success'
        elif self.cars < 0.95 * self.capacity:
            return 'warning'
        else:
            return 'danger'


__all__ = ['Lot']
