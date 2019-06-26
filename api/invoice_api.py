from flask import Blueprint, jsonify, request, Response
from dbservice.invoicedb import addInvoice, getInvoices
#from ..dbservice.invoicedb import *
import datetime
import json
from dbservice.models import Invoice

invoice_api = Blueprint('invoice_api', __name__)

@invoice_api.route("/invoices", methods=['GET'])
def listInvoices():
    data = getInvoices()
    invcs = []
    for inv in Invoice.__dict__:
        if (not str(inv).startsWith('__')):
            invcs.append(inv)
    print(invcs)
    js = jsonify(invcs)
    print(js)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'
    return resp

@invoice_api.route("/invoices/<invId>", methods=['GET'])
def getInvoice(invId):
    print(invId)
    inv = [ inv for inv in invDb if (inv['id'] == invId) ]
    return jsonify(inv[0])

@invoice_api.route("/invoices", methods=['POST'])
def createInvoice():
    inv = {
    'id':request.json['id'],
    'customerName':request.json['customerName'],
    'contactNo':request.json['contactNo'],
    'invoiceDate':request.json['invoiceDate'],
    'total':request.json['total']
    }
    invDb.append(inv)
    return jsonify(inv)

@invoice_api.route('/invoices/<empId>',methods=['DELETE'])
def deleteInvoice(invId):
    em = [ inv for inv in invDb if (inv['id'] == invId) ]
    if len(em) == 0:
       abort(404)
    invDb.remove(em[0])
    return jsonify({'response':'Success'})
