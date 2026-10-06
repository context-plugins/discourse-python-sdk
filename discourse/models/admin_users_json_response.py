from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .approved_by import ApprovedBy, ApprovedByDict
from .group10 import Group10, Group10Dict
from .penalty_counts import PenaltyCounts, PenaltyCountsDict
from .tl3_requirements import Tl3Requirements, Tl3RequirementsDict
from .upcoming_changes_stat import UpcomingChangesStat, UpcomingChangesStatDict


class AdminUsersJsonResponse(SdkBaseModel):
    id: int
    username: str
    name: str | None
    avatar_template: str
    active: bool
    admin: bool
    moderator: bool
    last_seen_at: str | None
    last_emailed_at: str | None
    created_at: str
    last_seen_age: float | None
    last_emailed_age: float | None
    created_at_age: float | None
    trust_level: int
    manual_locked_trust_level: str | None
    title: str | None
    time_read: int
    staged: bool
    days_visited: int
    posts_read_count: int
    topics_entered: int
    post_count: int
    associated_accounts: Optional[list[Any]] = UNSET
    can_send_activation_email: bool
    can_activate: bool
    can_deactivate: bool
    can_change_trust_level: Optional[bool] = UNSET
    ip_address: str
    registration_ip_address: str | None
    can_grant_admin: bool
    can_revoke_admin: bool
    can_grant_moderation: bool
    can_revoke_moderation: bool
    can_impersonate: bool
    like_count: int
    like_given_count: int
    topic_count: int
    flags_given_count: int
    flags_received_count: int
    private_topics_count: int
    can_delete_all_posts: bool
    can_be_deleted: Optional[bool] = UNSET
    can_be_anonymized: bool
    can_be_merged: bool
    full_suspend_reason: str | None
    latest_export: OptionalNullable[Any] = UNSET
    full_silence_reason: OptionalNullable[str] = UNSET
    silence_reason: OptionalNullable[str] = UNSET
    post_edits_count: OptionalNullable[int] = UNSET
    primary_group_id: int | None
    badge_count: int
    warnings_received_count: int
    bounce_score: int | None
    reset_bounce_score_after: str | None
    can_view_action_logs: bool
    can_disable_second_factor: bool
    can_delete_sso_record: bool
    api_key_count: int
    similar_users_count: Optional[int] = UNSET
    single_sign_on_record: str | None
    approved_by: ApprovedBy | None
    suspended_by: str | None
    silenced_by: str | None
    penalty_counts: Optional[PenaltyCounts] = UNSET
    next_penalty: Optional[str] = UNSET
    tl3_requirements: Optional[Tl3Requirements] = UNSET
    groups: list[Group10]
    external_ids: Any
    include_ip: bool
    upcoming_changes_stats: Optional[list[UpcomingChangesStat]] = UNSET


class AdminUsersJsonResponseDict(TypedDict):
    id: int
    username: str
    name: str | None
    avatar_template: str
    active: bool
    admin: bool
    moderator: bool
    last_seen_at: str | None
    last_emailed_at: str | None
    created_at: str
    last_seen_age: float | None
    last_emailed_age: float | None
    created_at_age: float | None
    trust_level: int
    manual_locked_trust_level: str | None
    title: str | None
    time_read: int
    staged: bool
    days_visited: int
    posts_read_count: int
    topics_entered: int
    post_count: int
    associated_accounts: NotRequired[list[Any]]
    can_send_activation_email: bool
    can_activate: bool
    can_deactivate: bool
    can_change_trust_level: NotRequired[bool]
    ip_address: str
    registration_ip_address: str | None
    can_grant_admin: bool
    can_revoke_admin: bool
    can_grant_moderation: bool
    can_revoke_moderation: bool
    can_impersonate: bool
    like_count: int
    like_given_count: int
    topic_count: int
    flags_given_count: int
    flags_received_count: int
    private_topics_count: int
    can_delete_all_posts: bool
    can_be_deleted: NotRequired[bool]
    can_be_anonymized: bool
    can_be_merged: bool
    full_suspend_reason: str | None
    latest_export: NotRequired[Any | None]
    full_silence_reason: NotRequired[str | None]
    silence_reason: NotRequired[str | None]
    post_edits_count: NotRequired[int | None]
    primary_group_id: int | None
    badge_count: int
    warnings_received_count: int
    bounce_score: int | None
    reset_bounce_score_after: str | None
    can_view_action_logs: bool
    can_disable_second_factor: bool
    can_delete_sso_record: bool
    api_key_count: int
    similar_users_count: NotRequired[int]
    single_sign_on_record: str | None
    approved_by: ApprovedByDict | None
    suspended_by: str | None
    silenced_by: str | None
    penalty_counts: NotRequired[PenaltyCountsDict]
    next_penalty: NotRequired[str]
    tl3_requirements: NotRequired[Tl3RequirementsDict]
    groups: list[Group10Dict]
    external_ids: Any
    include_ip: bool
    upcoming_changes_stats: NotRequired[list[UpcomingChangesStatDict]]
