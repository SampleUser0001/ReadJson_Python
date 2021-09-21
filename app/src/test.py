from dataclasses import dataclass, field, asdict
from typing import List
 
@dataclass
class SampleInfoChild:
  """ Sample情報子データクラス
  """
  childint: int = 0
  childstr: str = ''
 
@dataclass
class SampleInfoParent:
  """ Sample情報親データクラス
  """
  data1: int = 0
  data2: str = ''
  data3: float = 0.0
  listint: List[int] = field(default_factory=list)
  childobj: SampleInfoChild = None

def print_obj(obj):
  print("type : {}".format(type(obj)))
  print("obj : {}".format(obj))
  print()

if __name__ == '__main__':
  # dataclassのインスタンス生成
  sample_dataclass = SampleInfoParent(2, 'abc', 2.5, [123, 234], SampleInfoChild(2, 'ddd'))
  print_obj(sample_dataclass)

  # dataclass -> dict
  sample_dict = asdict(sample_dataclass)
  print_obj(sample_dict)

  # dict -> dataclass
  dict_to_dataclass = SampleInfoParent(**sample_dict)
  print_obj(dict_to_dataclass)