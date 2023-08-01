"""
Common utility function that could be used across bot
"""

# Built in imports
import os
import importlib
import tempfile

# Local imports
from . import constants as Key

def get_root_dir():
    """
    Return the bot root directory

    Returns:
        str
    """
    return os.environ[Key.ROOT_DIR_PATH]

def str_to_class(module_string):
    """
    Converts str into a python object

    Args:
        module_string (str): Module is str format. eg: 'a.b.c'

    Returns:
        Python Module
    """
    modstr, classstr = module_string.rsplit('.', 1)
    mod = importlib.import_module(modstr)
    return getattr(mod, classstr)

def mktempdir():
    """
    Make a temp directory
    """
    return tempfile.mkdtemp()

def write_file(content, filename, ext, dirpath=None):
    """
    Make a temp dir and write the content to a file
    """
    tmpfile = tempfile.NamedTemporaryFile(mode='w',
                                          suffix='.{}'.format(ext),
                                          prefix=filename,
                                          delete=False,
                                          dir=dirpath)

    with open(tmpfile.name, 'w') as fobj:
        fobj.write(content)

    return tmpfile
