from musical_app import db

class Musical(db.Model):
    __tablename__ = 'musical'

    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    runtime = db.Column(db.String)
    showtime = db.Column(db.String)
    rating = db.Column(db.String)
    price = db.Column(db.String)
    casting = db.Column(db.String)
    url = db.Column(db.String)

    theater_id = db.Column(db.Integer, db.ForeignKey('theater.id'))

    def __repr__(self):
        return f"Musical {self.num}"
