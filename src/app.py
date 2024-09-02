from flask import Flask
from routes import brand_api

app = Flask(__name__)
app.register_blueprint(brand_api)

if __name__ == '__main__':
    app.run(debug=True)
