from core.Router import Router

class API:

    def __init__(self):
        self.router = Router()

    def route(self, route, allowed_methods=['GET'], login_required=True):
        def decorator_api_route(func):
            for method in allowed_methods:
                self.router.add_route(route, method, func, login_required)
            def inner(*args, **kwargs):
                response = func(*args, **kwargs)
                return response
            return inner
        return decorator_api_route

    def request(self):
        pass

    def route_exists(self):
        pass

    def is_login_required(self) ->bool:
        return True

if __name__ == '__main__':
    test = API()
    test.route()