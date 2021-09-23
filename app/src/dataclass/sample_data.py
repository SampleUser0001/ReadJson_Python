# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
import datetime
from typing import List

@dataclass
class Piyo01:
  piyo11: str
  piyo12: str

@dataclass
class Fuga01:
  fuga11: str
  fuga12: str

@dataclass
class SampleJsonData:
  hoge01: str = None
  piyo01: Piyo01 = None
  fuga01: List[Fuga01] = field(default_factory=list)
  notDefinedInJsonStr: str = None
  sampleDate: datetime = None
  sampleInteger: int = None
  sampleBool: bool = None
  notDefinedInJsonBool: bool = None
