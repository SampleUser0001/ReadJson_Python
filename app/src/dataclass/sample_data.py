# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import List

@dataclass
class Piyo01:
  piyo11: str
  piyo12: str
  notDefinedInJson: str = None
  
@dataclass
class Fuga01:
  fuga11: str
  fuga12: str
  notDefinedInJson: str = None

@dataclass
class SampleJsonData:
  hoge01: str = ''
  piyo01: Piyo01 = None
  fuga01: List[Fuga01] = field(default_factory=list)
  notDefinedInJson: str = None
