from flask import Blueprint, jsonify, request
from app.models import db
from datetime import datetime
 
instagram_api = Blueprint('instagram', __name__, url_prefix='instagram') 

@instagram_api.route('/') 
def health():
    """Return a status of 'ok' if the server is running and listening to request"""
    return jsonify({"status": "ok"})

