# -*- coding: utf-8 -*-
import json
from dataclass.live import *

class Live:
  @staticmethod
  def import_file(import_file_path):
    with open(import_file_path, mode='r') as f:
      live_comment = LiveComment.from_dict(json.load(f))
    
    print(type(live_comment))
    print(type(live_comment.items[0].id))
    print(type(live_comment.items[0]))
    print(type(live_comment.items[0].snippet))
    
    item_list = []
    for item in live_comment.items:
      item_list.append(item)

    print(len(item_list))
    