from flask import Flask
from api.invoice_api import invoice_api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(invoice_api)


if __name__ == "__main__":
    app.run()    
