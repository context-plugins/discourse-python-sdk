from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Group(SdkBaseModel):
    name: str
    full_name: Optional[str] = UNSET
    bio_raw: Optional[str] = UNSET
    """About Group"""

    usernames: Optional[str] = UNSET
    """comma,separated"""

    owner_usernames: Optional[str] = UNSET
    """comma,separated"""

    automatic_membership_email_domains: Optional[str] = UNSET
    """pipe|separated"""

    visibility_level: Optional[int] = UNSET
    primary_group: Optional[bool] = UNSET
    flair_icon: Optional[str] = UNSET
    flair_upload_id: Optional[int] = UNSET
    flair_bg_color: Optional[str] = UNSET
    public_admission: Optional[bool] = UNSET
    public_exit: Optional[bool] = UNSET
    default_notification_level: Optional[int] = UNSET
    muted_category_ids: Optional[list[int]] = UNSET
    regular_category_ids: Optional[list[int]] = UNSET
    watching_category_ids: Optional[list[int]] = UNSET
    tracking_category_ids: Optional[list[int]] = UNSET
    watching_first_post_category_ids: Optional[list[int]] = UNSET


class GroupDict(TypedDict):
    name: str
    full_name: NotRequired[str]
    bio_raw: NotRequired[str]
    usernames: NotRequired[str]
    owner_usernames: NotRequired[str]
    automatic_membership_email_domains: NotRequired[str]
    visibility_level: NotRequired[int]
    primary_group: NotRequired[bool]
    flair_icon: NotRequired[str]
    flair_upload_id: NotRequired[int]
    flair_bg_color: NotRequired[str]
    public_admission: NotRequired[bool]
    public_exit: NotRequired[bool]
    default_notification_level: NotRequired[int]
    muted_category_ids: NotRequired[list[int]]
    regular_category_ids: NotRequired[list[int]]
    watching_category_ids: NotRequired[list[int]]
    tracking_category_ids: NotRequired[list[int]]
    watching_first_post_category_ids: NotRequired[list[int]]
