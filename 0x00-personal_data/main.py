#!/usr/bin/env python3

"""
Main file
"""

# import logging
# import re

# RedactingFormatter = __import__('filtered_logger').RedactingFormatter

# message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
# log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
# formatter = RedactingFormatter(fields=("email", "ssn", "password"))
# print(formatter.format(log_record))
"""
Main file
"""
# import logging

# get_logger = __import__('filtered_logger').get_logger
# PII_FIELDS = __import__('filtered_logger').PII_FIELDS

# print(get_logger.__annotations__.get('return'))
# print("PII_FIELDS: {}".format(len(PII_FIELDS)))


"""
Main file
"""

get_db = __import__('filtered_logger').get_db

db = get_db()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()
