from django.db import models

# Create your models here.

class Query_broker:
    def __init__(self, req, resp):
        self.req = req
        self.resp = resp
