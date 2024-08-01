#!/usr/bin/env python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('myapp.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def main():
    logger.info('started')
    logger.info('finished')

if __name__ == '__main__':
    main()
