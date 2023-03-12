import datetime
from . import db

class InstagramPosts(db.Model):

    __tablename__ = 'instagram_posts'

    # ID
    id = db.Column(db.Integer, primary_key=True)

    # Post description
    description = db.Column(db.String(120), nullable=True)

    # Image path
    image_path = db.Column(db.String(200), nullable=False)

    # Autdit timestamps
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Helper method to convert the model to a dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            }

    def __repr__(self):
        return f'<Instagram Post : {self.id} {self.image_path} {self.description}>'