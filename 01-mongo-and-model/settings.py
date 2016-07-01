MONGO_HOST = 'mongodb'
MONGO_DBNAME = 'usuario00'
people_schema = {
            'firstname': {'type': 'string'}
}
people = {
            'resource_methods': ['GET', 'POST', 'DELETE'],
            'schema': people_schema
}
DOMAIN = {'people': people}
