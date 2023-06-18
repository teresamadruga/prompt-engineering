import configparser
import os

from dotenv import find_dotenv, load_dotenv


def get_key_from_file(key, filepath):
    """
    Retrieves a key from a configuration file.

    Args:
        key (str): The key to retrieve.
        filepath (str): The path to the configuration file.

    Returns:
        str: The value associated with the key.
    """
    cfg = configparser.ConfigParser()
    cfg.read(filepath)
    return cfg.get("KEYS", key, fallback=f"{key} is not defined")


def get_key_from_env(key):
    """
    Retrieves a key from the environment variables.

    Args:
        key (str): The key to retrieve.

    Returns:
        str: The value associated with the key.
    """
    _ = load_dotenv(find_dotenv())
    return os.getenv(key)
