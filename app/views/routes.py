from flask import Blueprint, jsonify, request
from datetime import datetime
from app.models import db
from app.models.instagram_post import InstagramPosts
from app.models.queue import Queue
from app.models.social_platforms import SocialPlatforms
 
api = Blueprint('api', __name__, url_prefix='/api/v1') 
 
@api.route('/') 
def health():
    """Return a status of 'ok' if the server is running and listening to request"""
    return jsonify({"status": "ok"})
