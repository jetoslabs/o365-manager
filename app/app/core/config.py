import os

import yaml
from loguru import logger
from pydantic import BaseModel

from app.core.settings import settings


class GlobalConfig(BaseModel):
    tenant: str

    db_url: str
    db_pwd: str
    db_sales97_name: str
    db_fit_name: str
    db_mailstore_name: str

    aws_access_key_id: str
    aws_access_secret: str
    aws_region: str
    aws_output: str
    s3_root_bucket: str
    s3_default_object_prefix: str
    disk_base_path: str


class GlobalConfigHelper:
    @staticmethod
    def _load_global_config(filepath: str) -> GlobalConfig:
        try:
            with open(filepath) as file:
                global_config_dict = yaml.safe_load(file)
                config = GlobalConfig(**global_config_dict)
                return config
        except Exception as e:
            logger.bind().error(f"cwd={os.getcwd()}")
            logger.bind().error("Error while loading global_config... exiting")
            raise e


# TODO: move var
# global_config = GlobalConfigHelper._load_global_config("../configuration/global_config.yml")
global_config = GlobalConfigHelper._load_global_config(
    f"{settings.CONFIGURATION_PATH}configuration/global_config.yml"
)
