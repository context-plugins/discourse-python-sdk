from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UserAction(SdkBaseModel):
    excerpt: str
    action_type: int
    created_at: str
    avatar_template: str
    acting_avatar_template: str
    slug: str
    topic_id: int
    target_user_id: int
    target_name: str | None
    target_username: str
    post_number: int
    post_id: str | None
    username: str
    name: str | None
    user_id: int
    acting_username: str
    acting_name: str | None
    acting_user_id: int
    title: str
    deleted: bool
    hidden: str | None
    post_type: str | None
    action_code: str | None
    category_id: int
    closed: bool
    archived: bool


class UserActionDict(TypedDict):
    excerpt: str
    action_type: int
    created_at: str
    avatar_template: str
    acting_avatar_template: str
    slug: str
    topic_id: int
    target_user_id: int
    target_name: str | None
    target_username: str
    post_number: int
    post_id: str | None
    username: str
    name: str | None
    user_id: int
    acting_username: str
    acting_name: str | None
    acting_user_id: int
    title: str
    deleted: bool
    hidden: str | None
    post_type: str | None
    action_code: str | None
    category_id: int
    closed: bool
    archived: bool
