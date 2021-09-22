class LambdaHandler:
    '''
    Base lambda handler, that routes API gateway events to required endpoints and catches exceptions
    for unified error responses
    '''
    def __init__(self, api):
        self.api = api

    def handle(self, event, context):
        print(self.api)
        print(event)

