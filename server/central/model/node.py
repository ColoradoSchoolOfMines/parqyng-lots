# -*- coding: utf-8 -*-
"""Node model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, DateTime
from sqlalchemy.orm import relationship, backref

from central.model import DeclarativeBase, metadata, DBSession

class Node(DeclarativeBase):
    __tablename__ = 'nodes'

    id = Column(Integer, primary_key=True)
    key = Column(Integer, nullable=False, unique=True, index=True)
    last = Column(DateTime)

    lot_id = Column(Integer, ForeignKey('lots.id'))
    lot = relationship('Lot', back_populates='nodes')

__all__ = ['Node']
