MONGO_HOST = 'mongodb'
MONGO_DBNAME = 'usuario00'
stock_change_schema = {
    'product': {
        'type': 'string',
        'maxlength': 64,
        'required': True,
    },
    'person': {
        'type': 'string',
        'maxlength': 16,
    },
    'change': {
        'type': 'integer',
        'required': True,
    }
}
stock_change = {
    'schema': stock_change_schema,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET'],
}
DOMAIN = {
    'stock_change': stock_change,
}
