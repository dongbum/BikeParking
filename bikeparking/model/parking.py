# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from bikeparking.model import Base

class Parking(Base):
    __tablename__ = 'parking'

    no = Column(Integer, primary_key=True)
    address = Column(String(1024), unique=False)
    operating_time = Column(String(1024), unique=False)
    operating_agency = Column(String(1024), unique=False)
    parking_count = Column(String(1024), unique=False)
    parking_type = Column(String(1024), unique=False)
    charge = Column(Integer, unique=False)
    url = Column(String(1024), unique=False)
    phone = Column(String(1024), unique=False)

    def __init__(self, no, address, operating_time, operating_agency, parking_count, parking_type, charge, url, phone):
        self.no = no
        self.address = address
        self.operating_time = operating_time
        self.operating_agency = operating_agency
        self.parking_count = parking_count
        self.parking_type = parking_type
        self.charge = charge
        self.url = url
        self.phone = phone

    def __repr__(self):
        return '<Address %r>' & (self.address)