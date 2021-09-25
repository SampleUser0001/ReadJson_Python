# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
import datetime
from typing import List

@dataclass
class Piyo01:
  piyo11: str = None
  piyo12: str = None

@dataclass
class Fuga01:
  fuga11: str = None
  fuga12: str = None

@dataclass_json
@dataclass
class SampleJsonData:
  hoge01: str = None
  piyo01: Piyo01 = None
  fuga01: List[Fuga01] = field(default_factory=list)
  notDefinedInJsonStr: str = '' # 存在しない可能性がある値は
  sampleDate: datetime = None
  sampleInteger: int = None
  sampleBool: bool = None
  notDefinedInJsonBool: bool = False
  intlist: List[int] = field(default_factory=list)
