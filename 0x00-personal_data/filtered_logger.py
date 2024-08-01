#!/usr/bin/env python3
"logger module"

from typing import List
def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    "filter datum"
    messages: List[str] = message.split(separator)
    i: int = 0
    for m in messages:
        if m.split('=')[0] in fields:
            m = m.replace(m.split('=')[1], redaction)
            messages[i] = m
        i += 1
    return separator.join(messages)
