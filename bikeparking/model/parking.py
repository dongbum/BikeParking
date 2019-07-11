# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String

from bikeparking.model import Base

class Parking(Base):
    __tablename__ = 'parking'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    no = Column(Integer, primary_key=True)
    name = Column(String(1024), unique=False)
    address = Column(String(1024), unique=False)
    operating_time = Column(String(1024), unique=False)
    operating_agency = Column(String(1024), unique=False)
    parking_count = Column(String(1024), unique=False)
    parking_type = Column(String(1024), unique=False)
    charge = Column(Integer, unique=False)
    url = Column(String(1024), unique=False)
    phone = Column(String(1024), unique=False)

    def __init__(self, no, name, address, operating_time, operating_agency, parking_count, parking_type, charge, url, phone):
        self.no = no
        self.name = name
        self.address = address
        self.operating_time = operating_time
        self.operating_agency = operating_agency
        self.parking_count = parking_count
        self.parking_type = parking_type
        self.charge = charge
        self.url = url
        self.phone = phone

    def __repr__(self):
        return '<name %r Address %r>' & (self.name, self.address)