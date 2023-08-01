"""
Module to resolve yaml files
"""

# Built in imports
from future.utils import raise_from
from pathlib2 import Path

# Project specific imports
from omegaconf import OmegaConf
import yaml

# Local imports
from .exceptions import YAMLResolveError

def resolve(config_files):
    """Creates and returns key/value pairs from found in `config_files

    Args:
        config_files (list(str)): List of configuration files

    Returns:
        dict
    """
    confs = []
    for config_file in config_files:
        # Omegaconf only accepts str file paths.
        if isinstance(config_file, Path):
            config_file = str(config_file)
        try:
            confs.append(OmegaConf.load(config_file))
        except yaml.scanner.ScannerError as exc:
            raise_from(YAMLResolveError("Failed to load config"), exc)

    return OmegaConf.merge(*confs)

def save(config, filepath):
    """
    Save the config to the disk
    """
    OmegaConf.save(config=config, f=filepath)
    return filepath
