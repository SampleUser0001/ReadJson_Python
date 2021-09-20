# -*- coding: utf-8 -*-
from enum import Enum

class Top(Enum):
  KEY = "kind"
  ETAG = "etag"
  POLLING_INTERVAL_MILLIS = "pollingIntervalMillis"
  PAGE_INFO = ("pageInfo", ["totalResults", "resultsPerPage"])
  NEXT_PAGE_TOKEN = "nextPageToken"
  ITEMS = ("items", ["kind", "etag", "id", "snippet"])

class NextPageToken(Enum):
  TOTAL_RESULTS = "totalResults"
  RESULTS_PER_PAGE = "resultsPerPage"

class Items(Enum):
  KIND = "kind"
  ETAG = "etag"
  ID = "id"
  SNIPPET = "snippet"