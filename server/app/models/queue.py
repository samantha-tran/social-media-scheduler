import datetime
from . import db

class Queue(db.Model):

    __tablename__ = 'queue'

    # Post ID
    postId = db.Column(db.Integer, primary_key=True)

    # Social media platform ID
    platformID = db.Column(db.Integer, primary_key=True)

    # Scheduled time to release the post
    scheduled_time = db.Column(db.DateTime, nullable=True)

    # Whether scheduled post has been completed
    completed = db.Column(db.Boolean, nullable=False, default=False)
    
    # Audit timestamps
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Helper method to convert the model to a dictionary
    def to_dict(self):
        return {
            'postID': self.title,
            'platformID': self.description,
            'scheduled_time': self.deadline_at.isoformat() if self.deadline_at else None,
            'completed': self.completed,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            }

    def __repr__(self):
        return f'<Queued Item : {self.postId} {self.platformID} {self.scheduled_time} {self.completed}>'