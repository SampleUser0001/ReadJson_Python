# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os
import json

from dataclass.sample_data import *

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

  # dataclassesモジュールを使用した変換。
  sample_json_data = SampleJsonData(**sample_dict)
  print(sample_json_data)
  
  print(type(sample_json_data))
  # list[int]みたいなプリミティブな型は問題ないが…
  print(type(sample_json_data.intlist[0]))

  # list[Fuga01]みたいな自作クラスを含めた変換ができない。dictになる。
  print(type(sample_json_data.fuga01[0]))
  
  # こちらはlistを含めていないが、自作クラスを含めた変換はやはりできない。dictになる。
  print(type(sample_json_data.piyo01))
  
  fuga01 = Fuga01(**sample_json_data.fuga01[0])
  print(type(fuga01))
  
  tmp = None
  
  # こっちが正解。dataclasses_jsonモジュールを使用した変換。
  sample_json_data_2 = SampleJsonData.from_dict(sample_dict)
  print(sample_json_data_2)

  print('type(notDefinedInJsonInt) : {}'.format(type(sample_json_data_2.notDefinedInJsonInt)))
  print('type(notDefinedInJsonStr) : {}'.format(type(sample_json_data_2.notDefinedInJsonStr)))
  print('type(notDefinedInJsonBool) : {}'.format(type(sample_json_data_2.notDefinedInJsonBool)))
  print('type(notDefinedInJsonDatetime) : {}'.format(type(sample_json_data_2.notDefinedInJsonDatetime)))
  print('type(notDefinedInJsonListFuga01) : {}'.format(type(sample_json_data_2.notDefinedInJsonListFuga01)))