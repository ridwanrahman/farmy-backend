class Request:
    def __init__(self, http_method, route,
                 headers={}, query_string_parameters={},
                 path_parameters={}, body=None):
        self.http_method = http_method
        self.route = route
        self.headers = headers
        self.query_string_parameters = query_string_parameters
        self.path_parameters = path_parameters
        self.body = body
