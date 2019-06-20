from flask import Flask
from api.invoice_api import invoice_api
from flask_cors import CORS

app = Flask(__name__)
#to suppord CORS
CORS(app)
#to add endpoints defined in different file
app.register_blueprint(invoice_api)


if __name__ == "__main__":
    app.run()    
