from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # connect to all the items that have the store_id of the specific store
    # lazy="dynamic" : items fetch only if we specify explicitly, and not every time we fetch a store
    # cascade="all, delete" : delete all the items of the store when delete a store
    items = db.relationship(
        "ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")

    tags = db.relationship(
        "TagModel", back_populates="store", lazy="dynamic", cascade="all, delete")
