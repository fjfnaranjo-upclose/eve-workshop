MONGO_HOST = 'mongodb'
MONGO_DBNAME = 'usuario00'
people_schema = {
    'name': {
        'type': 'string',
        'minlength': 8,
        'maxlength': 32,
        'required': True,
        'unique': True,
    },
    'born': {
        'type': 'datetime',
    }
}
people = {
    'item_title': 'person',
    'schema': people_schema,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PATCH'],
    'additional_lookup': {
        'url': 'regex("[\w.]+")',
        'field': 'name'
    },
}
DOMAIN = {
    'people': people
}
