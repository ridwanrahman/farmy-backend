class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, route, http_method, func, login_required):
        if route not in self.routes:
            self.routes[route] = {}

        self.routes[route][http_method] = {
            'function': func,
            'login_required': login_required
        }

    def another(self):
        pass

