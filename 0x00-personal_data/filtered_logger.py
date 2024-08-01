#!/usr/bin/env python3
"""
filter module
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    "filter datum function"
    for f in fields:
        m = re.sub(f'{f}=.+?{separator}',
                   f'{f}={redaction}{separator}', message)
    return message
