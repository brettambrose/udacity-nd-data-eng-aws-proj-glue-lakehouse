import os 
import configparser

def load_config(path):
    """Read an INI-style config file and return a configparser object"""
    config = configparser.ConfigParser()
    config.read(path)
    return config, path

def load_main_config(path="lakehouse.cfg"):
    return load_config(path)

def load_aws_credentials():
    path = os.path.expanduser(os.path.join("~", ".aws", "credentials"))
    return load_config(path)


def load_aws_config():
    path = os.path.expanduser(os.path.join("~", ".aws", "config"))
    return load_config(path)