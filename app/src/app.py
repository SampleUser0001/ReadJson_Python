# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os
import json

from dataclass.sample_data import *

import sys
sys.path.append('./')
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

# IMPORT_FILE_PATH = PYTHON_APP_HOME + '/file/comments_7K1WZ5Sfgw0_20210911_215902.json'
IMPORT_FILE_PATH = PYTHON_APP_HOME + '/file/sample.json'

if __name__ == '__main__':
  # .envの取得
  # setting.ENV_DIC[ImportEnvKeyEnum.importenvに書いた値.value]
  
  # 起動引数の取得
  # args = sys.argv
  # args[0]はpythonのファイル名。
  # 実際の引数はargs[1]から。
  
  with open(IMPORT_FILE_PATH, mode='r') as f:
    sample_dict = json.load(f)

#  print(Top.KEY.value)
#  print(Top.PAGE_INFO.value)
  
  sample_data_json = SampleJsonData(**sample_dict)
  print(sample_data_json)
  