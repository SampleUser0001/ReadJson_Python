# -*- coding: utf-8 -*-
import os
import glob
import json
from dataclass.live import *

class Merge:
  @staticmethod
  def import_file(import_file_path):
    before_merge_list = []
    before_merge_comment_length = 0
    for file in [p for p in glob.glob(import_file_path + '/**' , recursive=True) if (os.path.isfile(p) and os.path.splitext(p)[1][1:] == 'json')]:
      with open(file, mode='r') as f:
        live_comment = LiveComment.from_dict(json.load(f))

      comment_length = len(live_comment.items)
      before_merge_comment_length += comment_length
      before_merge_list.append(live_comment.items)
      print('file : {} , len : {}'.format(file, comment_length))
    
    print( \
      'file count : {} , before_merge_comment_length : {}'.format( \
        len(before_merge_list), before_merge_comment_length
      )
    )
    merge_list = []
    for items in before_merge_list:
      for item in items:
        merge_list.append(item)
    
    merge_list = list(set(merge_list))
    print('after merge len : {}'.format(len(merge_list)))