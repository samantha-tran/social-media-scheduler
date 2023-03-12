import datetime
from . import db
class SocialPlatforms(db.Model):

    __tablename__ = 'social_platforms'

    # ID
    id = db.Column(db.Integer, primary_key=True)

    # Name of the social media platform
    name = db.Column(db.String(80), nullable=False)

    # Audit timestamps
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # helper method to convert the model to a dictionary
    def to_dict(self):
        return {
        'id': self.id,
        'name': self.title,
        'created_at': self.created_at.isoformat() if self.created_at else None,
        'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
    
    def __repr__(self):
        return f'<Social Media Platform : {self.id} {self.name}>'