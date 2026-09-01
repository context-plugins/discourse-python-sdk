from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PostsJsonRequest(SdkBaseModel):
    title: Optional[str] = UNSET
    """Required if creating a new topic or new private message."""

    raw: str
    topic_id: Optional[int] = UNSET
    """Required if creating a new post."""

    category: Optional[int] = UNSET
    """Optional if creating a new topic, and ignored if creating a new post."""

    target_recipients: Optional[str] = UNSET
    """Required for private message, comma separated."""

    target_usernames: Optional[str] = UNSET
    """Deprecated. Use target_recipients instead."""

    archetype: Optional[str] = UNSET
    """Required for new private message."""

    created_at: Optional[str] = UNSET
    reply_to_post_number: Optional[int] = UNSET
    """Optional, the post number to reply to inside a topic."""

    embed_url: Optional[str] = UNSET
    """Provide a URL from a remote system to associate a forum topic with that URL, typically for using Discourse as a
    comments system for an external blog."""

    external_id: Optional[str] = UNSET
    """Provide an external_id from a remote system to associate a forum topic with that id."""

    auto_track: Optional[bool] = UNSET
    """If false, the user will not track the topic. By default, the user will track the topic."""


class PostsJsonRequestDict(TypedDict):
    title: NotRequired[str]
    raw: str
    topic_id: NotRequired[int]
    category: NotRequired[int]
    target_recipients: NotRequired[str]
    target_usernames: NotRequired[str]
    archetype: NotRequired[str]
    created_at: NotRequired[str]
    reply_to_post_number: NotRequired[int]
    embed_url: NotRequired[str]
    external_id: NotRequired[str]
    auto_track: NotRequired[bool]
