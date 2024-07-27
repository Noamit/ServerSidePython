from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    # auto-increment by defult
    id = db.Column(db.Integer, primary_key=True)
    # if we want items with an unique name, than add unique=True
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String())
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(
        db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False
    )
    # map store to the related store (by id) as we declared on StoreModel
    store = db.relationship("StoreModel", back_populates="items")

    # mant-to-many. each item can related to many tags.
    # secondary="items_tags" : in oreder to find the tags related to the item, we need items_tags table
    tags = db.relationship(
        "TagModel", back_populates="items", secondary="items_tags")
