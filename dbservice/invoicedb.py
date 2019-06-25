from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append("..")
from models import Invoice

engine = create_engine("sqlite:///rms-service.db", echo = True)

session = sessionmaker(bind=engine)

invoices = session.query(Invoice).all()
print(invoices)

session = Session()
