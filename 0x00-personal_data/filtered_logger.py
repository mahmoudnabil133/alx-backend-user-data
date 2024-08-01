#!/usr/bin/env python3
"""
filter module
"""
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    "filter datum function"
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Redacting Formatter class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields
    
    def format(self, record: logging.LogRecord) -> str:
        "format class method"
        record.msg = filter_datum(self.fields, self.REDACTION,
                                    record.getMessage(), self.SEPARATOR)
        return super().format(record)
