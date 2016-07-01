from flask import current_app
from eve import Eve
from eve.auth import BasicAuth
from json import dumps, loads


class UpcloseBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        is_admin = (username == 'alfonso' and password == 'epicmola81')
        is_person = (
            (username == 'naranjo' and password == 'eveeslomas') or
            (username == 'stanete' and password == 'spaceXXX93')
        )
        if (resource == 'product' and method == 'PATCH') and not is_admin:
            return False
        if is_admin or is_person:
            self.set_request_auth_value(username)
            return True
        return False


def stock_change_inject_person(request):
    payload = loads(request.data)
    payload["person"] = current_app.auth.get_request_auth_value()
    request.data = dumps(payload)
    return request


def before_insert(t, documents):
    print t
    for document in documents:
        print documents


app = Eve(auth=UpcloseBasicAuth)
#app.on_pre_POST_stock_change += stock_change_inject_person
app.on_insert_item += before_insert


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12000, debug=True)
