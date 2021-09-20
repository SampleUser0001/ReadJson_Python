from dataclasses import dataclass, field
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

