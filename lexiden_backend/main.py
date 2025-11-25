from flask import Flask, jsonify, request
from flask_cors import CORS

#internal imports
from Controllers import r
import Models

#helper function for app defn.
def create_app():
    app = Flask(__name__)

    #CORS is needed to conect to frontend
    CORS(app, 
         supports_credentials=True, 
         origins=["http://localhost:3000"]  #frontend URL
         ) 

    #app.config["SECRET_KEY"]=...
    app.register_blueprint(r, url_prefix="")

    return app


app = create_app()
app.run(host="0.0.0.0", port=5000, debug=True)