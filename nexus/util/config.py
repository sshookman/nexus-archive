"""Logging Config"""
import logging

LOG_LEVELS = list(logging._nameToLevel.keys())
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] <%(name)s> %(message)s"
DATE_FORMAT = "%Y-%m-%d %I:%M:%S"