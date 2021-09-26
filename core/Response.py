import json


class Response:
    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body = body

    def serialize(self):
        return {
            'status_code': self.status_code,
            'body': json.dumps(self.body)
        }
