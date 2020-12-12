import logging
import json
import time

from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection


def get_logger(name):
    logger = logging.getLogger(name.split(".")[0])
    logger.json = print_json
    return logger

def print_json(data):
    print(json.dumps(data, indent=2, sort_keys=False, cls=DjangoJSONEncoder))
