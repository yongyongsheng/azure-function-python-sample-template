import logging
import azure.functions as functions

def main(req: func.HttpRequest) -> func.HttpResponse: 
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse("Hello island");