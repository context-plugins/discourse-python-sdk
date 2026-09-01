from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .created_by import CreatedBy, CreatedByDict
from .last_poster import LastPoster, LastPosterDict
from .participant1 import Participant1, Participant1Dict


class Details(SdkBaseModel):
    can_edit: bool
    notification_level: int
    can_move_posts: bool
    can_delete: bool
    can_remove_allowed_users: bool
    can_create_post: bool
    can_reply_as_new_topic: bool
    can_invite_to: Optional[bool] = UNSET
    can_invite_via_email: Optional[bool] = UNSET
    can_flag_topic: Optional[bool] = UNSET
    can_convert_topic: bool
    can_review_topic: bool
    can_close_topic: bool
    can_archive_topic: bool
    can_split_merge_topic: bool
    can_edit_staff_notes: bool
    can_toggle_topic_visibility: bool
    can_pin_unpin_topic: bool
    can_banner_topic: Optional[bool] = UNSET
    can_moderate_category: bool
    can_remove_self_id: int
    participants: Optional[list[Participant1]] = UNSET
    created_by: CreatedBy
    last_poster: LastPoster


class DetailsDict(TypedDict):
    can_edit: bool
    notification_level: int
    can_move_posts: bool
    can_delete: bool
    can_remove_allowed_users: bool
    can_create_post: bool
    can_reply_as_new_topic: bool
    can_invite_to: NotRequired[bool]
    can_invite_via_email: NotRequired[bool]
    can_flag_topic: NotRequired[bool]
    can_convert_topic: bool
    can_review_topic: bool
    can_close_topic: bool
    can_archive_topic: bool
    can_split_merge_topic: bool
    can_edit_staff_notes: bool
    can_toggle_topic_visibility: bool
    can_pin_unpin_topic: bool
    can_banner_topic: NotRequired[bool]
    can_moderate_category: bool
    can_remove_self_id: int
    participants: NotRequired[list[Participant1 | Participant1Dict]]
    created_by: CreatedBy | CreatedByDict
    last_poster: LastPoster | LastPosterDict
