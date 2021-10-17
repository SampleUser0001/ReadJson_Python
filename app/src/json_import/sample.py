# -*- coding: utf-8 -*-
import json
from dataclass.sample_data import SampleJsonData, Piyo01, Fuga01

class Sample:
  @staticmethod
  def import_file(import_file_path):
    with open(import_file_path, mode='r') as f:
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
    print(type(sample_json_data_2))
    # これなら自作クラスになる。
    print(type(sample_json_data_2.fuga01[0]))
  
    print('type(notDefinedInJsonInt) : {}'.format(type(sample_json_data_2.notDefinedInJsonInt)))
    print('type(notDefinedInJsonStr) : {}'.format(type(sample_json_data_2.notDefinedInJsonStr)))
    print('type(notDefinedInJsonBool) : {}'.format(type(sample_json_data_2.notDefinedInJsonBool)))
    print('type(notDefinedInJsonDatetime) : {}'.format(type(sample_json_data_2.notDefinedInJsonDatetime)))
    print('type(notDefinedInJsonListFuga01) : {}'.format(type(sample_json_data_2.notDefinedInJsonListFuga01)))