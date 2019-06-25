from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dbservice import engine
from models import Invoice


Session = sessionmaker(bind = engine)
session = Session()

inv = Invoice()
inv.customerName = "Ashish"
inv.id = 1
inv.contactNo = 7208769992

session.add(inv)
session.commit()

invoices = session.query(Invoice).all()
print(invoices)

session = Session()
