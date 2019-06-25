from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, ARRAY
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Invoice1(Base):
    __table__ = 'invoice'
    id = Column(Integer, primary_key = True)
    customerName = Column(String)
    contactNo = Column(String)
    total = Column(Numeric)
    invoiceDate = Column(String)
    items = Column(ARRAY(String))
