from core.API import API
api = API()


@api.route('/users/authentication', allowed_methods=['GET'])
def authentication():
    print("auth")
    pass


@api.route('/users/login', allowed_methods=['POST'])
def login():
    pass


@api.route('/users/get_all', allowed_methods=['GET'])
def get_all_users():
    pass

if __name__ == '__main__':
    authentication()
