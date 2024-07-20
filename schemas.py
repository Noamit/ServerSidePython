from marshmallow import Schema, fields


# on create an item
class ItemSchema(Schema):
    # when data came from request, its not required. only when response data
    id = fields.Str(dump_only=True)
    # when data came from request, its required. those 3 required on request data and should be those types.
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


# on update an item none of the fields is required
class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


# on create a store
class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
