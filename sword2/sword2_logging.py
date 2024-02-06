#!/usr/bin/env python
"""
`sword2` logging
"""
import importlib.util
import logging.config
import os


try:
    sword2_path = importlib.util.find_spec("sword2").submodule_search_locations[0]
except (AttributeError, IndexError):
    sword2_path = ""
SWORD2_LOGGING_CONFIG = os.path.join(
    sword2_path, "data", "sword2_logging.conf"
)  # default

BASIC_CONFIG = """[loggers]
keys=root

[handlers]
keys=consoleHandler

[formatters]
keys=basicFormatting

[logger_root]
level=INFO
handlers=consoleHandler

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=basicFormatting
args=(sys.stdout,)

[formatter_basicFormatting]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
"""


def create_logging_config(pathtologgingconf=None):
    """
    If you want to use the sword logging configuration, you should call this to create the
    basic logging configuration (if you haven't provided it yourself in the /data/sword2_logging.conf
    file already.  This will write the basic config to the path provided, or to the SWORD2_LOGGING_CONFIG
    directory if no path is provided.  Directories will be created recursively as needed.
    """
    # set the path to default if none is provided
    if pathtologgingconf is None:
        pathtologgingconf = SWORD2_LOGGING_CONFIG

    # ensure that the path exists
    d = os.path.dirname(pathtologgingconf)
    os.makedirs(d)

    # write the basic config to the file
    fn = open(pathtologgingconf, "wb")
    fn.write(BASIC_CONFIG)
    fn.close()


# if not os.path.isfile(SWORD2_LOGGING_CONFIG):
#    create_logging_config(SWORD2_LOGGING_CONFIG)
#
# logging.config.fileConfig(SWORD2_LOGGING_CONFIG)

# when we call this module, load the logging configuration if it exists
if os.path.isfile(SWORD2_LOGGING_CONFIG):
    logging.config.fileConfig(SWORD2_LOGGING_CONFIG)
