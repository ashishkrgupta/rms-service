from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from dbservice import engine

metadata = MetaData()
metadata.bind = engine
Base = declarative_base()

class Invoice(Base):
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key = True)
    customerName = Column(String)
    contactNo = Column(String)
    total = Column(Numeric)
    invoiceDate = Column(String)
    items = Column(ARRAY(String))

metadata.create_all()