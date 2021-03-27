from musical_app import db

class Theater(db.Model):
    __tablename__ = 'theater'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    musicals = db.relationship('Musical', backref='theater', cascade = "all, delete, delete-orphan")

    def __repr__(self):
        return f"Theater {self.id}"
