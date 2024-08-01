#!/usr/bin/env python3
"logger module"
import re


def filter_datum(fields, redaction, message, separator):
    "filter datum"
    for f in fields:
        message = re.sub(f'{f}=.+?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message
