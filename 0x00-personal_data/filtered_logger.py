#!/usr/bin/env python3
"logger module"

def filter_datum(fields, redaction, message, separator):
    "filter datum"

    messages = message.split(separator)
    i = 0
    for m in messages:
        if m.split('=')[0] in fields:
            m = m.replace(m.split('=')[1], redaction)
            messages[i] = m
        i += 1
    return separator.join(messages)
