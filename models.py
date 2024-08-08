from datetime import datetime
from config import db

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String, nullable=False)
    service_name = db.Column(db.String, nullable=False)
    log_level = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)
    received_at = db.Column(db.DateTime, default=datetime.utcnow)
