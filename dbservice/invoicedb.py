from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .dbservice import engine
from .models import Invoice

Session = sessionmaker(bind = engine)

def addInvoice(invoice):
    session = Session()
    session.add(invoice)
    session.commit()

def getInvoices():
    session = Session()
    invoices = session.query(Invoice).all()
    return invoices

def getInvoice(invoiceId):
    session = Session()
    invoices = session.query(Invoice).all()
    return invoices
    
