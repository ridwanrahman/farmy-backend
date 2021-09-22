from core.LambdaHandler import LambdaHandler
from apps.users.service import api

user_lambda_handler = LambdaHandler(api=api)

def user_handler(event, context):
    return user_lambda_handler.handle(event, context)
