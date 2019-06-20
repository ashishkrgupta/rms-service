from flask import Flask
from api.invoice_api import invoice_api

app = Flask(__name__)
app.register_blueprint(invoice_api)


if __name__ == "__main__":
    app.run()    
