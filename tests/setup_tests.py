import configparser
import os
from pathlib import Path

file_path = Path(os.path.dirname(os.path.abspath(__file__)))

def read_api_from_config_ini(config_ini_path: str) -> str:
    config = configparser.ConfigParser()
    config_file_path = os.path.abspath(
        os.path.join(file_path.parents[0], config_ini_path)
    )
    config.read(os.path.join(config_file_path))
    return config["api_key"]["kbflow_api_key"]

def set_kbflow_api_environ_var(config_ini_path: str):
    api_key = read_api_from_config_ini(config_ini_path=config_ini_path)
    os.environ["KBFLOW_API"] = api_key