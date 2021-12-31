import json
from decimal import Decimal
import logging

logger = logging.getLogger(__file__)


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


def serialize_decimal(decimal):
    return json.dumps(decimal, cls=DecimalEncoder)


def log_info(string):
    logger.info(string)


def log_warning(string):
    logger.warn(string)


def log_error(string):
    logger.error(string)
