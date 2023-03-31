import os
from typing import Optional, Dict

import yaml

from app.core.logger import logger


def get_profile():
    """
    Returns the specified environment profile.
    :return: the profile.
    """
    return os.getenv('profile', 'local')


class Config:
    """
    Class for loading configuration settings from a base file and an environment specific file.
    """

    # The configuration settings
    config: dict = None

    def __init__(self):
        # Initialization
        env_config = {}

        # Load the base config file
        base_config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config', f'env-base.yml')
        if os.path.isfile(base_config_file_path):
            with open(base_config_file_path) as config_file:
                logger.info('Loading base configuration')
                self.config = yaml.safe_load(config_file)
        else:
            raise FileNotFoundError(f'Base configuration file {base_config_file_path} not found.')

        # Load the specific environment config file
        config_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '../config', f'env-{get_profile()}.yml')

        if os.path.isfile(config_file_path):
            with open(config_file_path, 'r') as config_file:
                logger.info(f'Loading environment configuration: {get_profile()}')
                env_config = yaml.safe_load(config_file)
        else:
            raise FileNotFoundError(f'Environment configuration file {config_file_path} not found.')

        # Merge the configurations together
        for k, v in env_config.items():
            # Check if the current key already exists in base config
            if k in self.config.keys():
                # If so, merge the dict content
                self.config[k] = dict(self.config[k], **env_config[k])
            else:
                # Otherwise, create it
                self.config[k] = env_config[k]

    def get_mongo(self) -> Optional[Dict]:
        """
        Returns the configuration settings for connecting to MongoDB.
        :return: the mongo settings.
        """

        try:
            return self.config['mongo']
        except Exception as e:
            logger.error(f'Error: {e}')
            return None

    def get_tesseract_path(self) -> Optional[str]:
        try:
            return self.config['tesseract']['path']
        except Exception as e:
            logger.error(f'Error: {e}')
            return None


# Instantiate the configuration
cfg = Config()
