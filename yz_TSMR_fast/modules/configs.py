import os
from typing import Union

# Union 可以輸入不同型別的變數
ME_CONFIG_MONGODB_SERVER: Union[None, str] = os.environ.get('ME_CONFIG_MONGODB_SERVER', 'mongoadmin')
ME_CONFIG_MONGODB_PORT: Union[None, str] = os.environ.get('ME_CONFIG_MONGODB_PORT', 27017)
MONGO_INITDB_ROOT_USERNAME: Union[None, str] = os.environ.get('MONGO_INITDB_ROOT_USERNAME', 'mongoadmin')
MONGO_INITDB_ROOT_PASSWORD: Union[None, str] = os.environ.get('MONGO_INITDB_ROOT_PASSWORD', 'mongodb')
