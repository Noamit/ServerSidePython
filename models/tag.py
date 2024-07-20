from db import db


class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    # we want the name to be unique but only in the same store so we will check tis manually
    name = db.Column(db.String(80), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey(
        "stores.id"), nullable=False)

    # one-to-many. each tag is related only to one store
    store = db.relationship("StoreModel", back_populates="tags")

    # mant-to-many. each tag can related to many items.
    # secondary="items_tags" : in oreder to find the itmes related to the tags, we need items_tags table
    items = db.relationship(
        "ItemModel", back_populates="tags", secondary="items_tags")
