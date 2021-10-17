# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os
import json
import sys

from dataclass.sample_data import *

from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting

from json_import.live import Live
from json_import.sample import Sample

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

LIVE_JSON = PYTHON_APP_HOME + '/file/comments_vAeWI2znekQ_20211017_221838.json'
SAMPLE_JSON = PYTHON_APP_HOME + '/file/sample.json'

if __name__ == '__main__':
  # .envの取得
  # setting.ENV_DIC[ImportEnvKeyEnum.importenvに書いた値.value]
  
  # 起動引数の取得
  # args = sys.argv
  # args[0]はpythonのファイル名。
  # 実際の引数はargs[1]から。
  
  args = sys.argv
  file_type = args[1]
  
  if file_type == 'live':
    Live.import_file(LIVE_JSON)
  elif file_type == 'sample':
    Sample.import_file(SAMPLE_JSON)

  
