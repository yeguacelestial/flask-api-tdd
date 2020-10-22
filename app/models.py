from app import db


# NOTE: Class names should always be plural
class Bucketlist(db.Model):
    """ This class represents the bucketlist table. """

    __tablename__ = 'bucketlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )

    def __init__(self, name):
        """ Initialize with name """
        self.name = name

    # 'save' method will be used to add a new bucketlist to DB
    def save(self):
        db.session.add(self)
        db.session.commit()

    # 'get_all' method is a static method to get all bucketlists in a single query
    @staticmethod
    def get_all():
        return Bucketlist.query.all()

    # 'delete' method, deletes an existing bucketlist from DB
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # __repr__ method represents object instance of this model
    def __repr__(self):
        return "<Bucketlist: {}>".format(self.name)
