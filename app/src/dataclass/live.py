# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
import datetime
from typing import List

@dataclass(unsafe_hash=True)
class MemberMilestoneChatDetails:
  memberLevelName: str = None
  memberMonth: int = None
  userComment: str = None

@dataclass(unsafe_hash=True)
class SuperStickerMetadata:
  stickerId: str = None
  altText: str = None
  altTextLanguage: str = None

@dataclass_json
@dataclass(unsafe_hash=True)
class SuperStickerDetails:
  amountMicros: str = None
  currency: str = None
  amountDisplayString:str = None
  tier: int = None
  superStickerMetadata: SuperStickerMetadata = None

@dataclass_json
@dataclass(unsafe_hash=True)
class SuperChatDetails:
  amountMicros: str = None
  currency: str = None
  amountDisplayString: str = None
  userComment: str = None
  tier: int = None

@dataclass_json
@dataclass(unsafe_hash=True)
class AuthorDetails:
  channelId: str = None
  channelUrl: str = None
  displayName: str = None
  profileImageUrl: str = None
  isVerified: bool = None
  isChatOwner: bool = None
  isChatSponsor: bool = None
  isChatModerator: bool = None

@dataclass(unsafe_hash=True)
class TextMessageDetails:
  messageText: str = None

@dataclass_json
@dataclass(unsafe_hash=True)
class Snippet:
  type: str = None
  liveChatId: str = None
  authorChannelId: str = None
  publishedAt: datetime = None
  hasDisplayContent: bool = None
  displayMessage: str = None
  textMessageDetails: TextMessageDetails = None
  superChatDetails: SuperChatDetails = None
  superStickerDetails: SuperStickerDetails = None
  memberMilestoneChatDetails: MemberMilestoneChatDetails = None

@dataclass_json
@dataclass(unsafe_hash=True)
class Item:
  kind: str = None
  etag: str = None
  id: str = None
  snippet: Snippet = None
  authorDetails: AuthorDetails = None

@dataclass(unsafe_hash=True)
class VideoIdAndComments:
  video_id: str = None
  comment_list: List[Item] = field(default_factory=list)

@dataclass(unsafe_hash=True)
class PageInfo:
  totalResults: int = None
  resultsPerPage: int = None

@dataclass_json
@dataclass(unsafe_hash=True)
class LiveComment:
  kind: str = None
  etag: str = None
  pollingIntervalMillis: int = None
  offlineAt: datetime = None
  pageInfo: PageInfo = None
  nextPageToken: str = None
  items: List[Item] = field(default_factory=list)
