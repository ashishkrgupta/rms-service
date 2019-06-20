from flask import Blueprint, jsonify, request
import datetime
import json

invoice_api = Blueprint('invoice_api', __name__)

invDb = [
    {
        'id':'1',
        'customerName':'Ashish',
        'contactNo':'1234567890',
        'invoiceDate':'',
        'total':122.2
    },
    {
        'id':'2',
        'customerName':'Raju',
        'contactNo':'0987654321',
        'invoiceDate':'',
        'total':112.03
    }
]

@invoice_api.route("/invoices", methods=['GET'])
def getInvoices():
    return jsonify({'invoices':invDb})

@invoice_api.route("/invoices/<invId>", methods=['GET'])
def getInvoice(invId):
    print(invId)
    inv = [ inv for inv in invDb if (inv['id'] == invId) ]
    return jsonify({'invoice':inv})

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
