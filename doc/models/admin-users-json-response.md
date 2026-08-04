
# Admin Users Json Response

## Structure

`AdminUsersJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |
| `active` | `bool` | Required | - |
| `admin` | `bool` | Required | - |
| `moderator` | `bool` | Required | - |
| `last_seen_at` | `str` | Required | - |
| `last_emailed_at` | `str` | Required | - |
| `created_at` | `str` | Required | - |
| `last_seen_age` | `float` | Required | - |
| `last_emailed_age` | `float` | Required | - |
| `created_at_age` | `float` | Required | - |
| `trust_level` | `int` | Required | - |
| `manual_locked_trust_level` | `str` | Required | - |
| `title` | `str` | Required | - |
| `time_read` | `int` | Required | - |
| `staged` | `bool` | Required | - |
| `days_visited` | `int` | Required | - |
| `posts_read_count` | `int` | Required | - |
| `topics_entered` | `int` | Required | - |
| `post_count` | `int` | Required | - |
| `associated_accounts` | `List[Any]` | Optional | - |
| `can_send_activation_email` | `bool` | Required | - |
| `can_activate` | `bool` | Required | - |
| `can_deactivate` | `bool` | Required | - |
| `can_change_trust_level` | `bool` | Optional | - |
| `ip_address` | `str` | Required | - |
| `registration_ip_address` | `str` | Required | - |
| `can_grant_admin` | `bool` | Required | - |
| `can_revoke_admin` | `bool` | Required | - |
| `can_grant_moderation` | `bool` | Required | - |
| `can_revoke_moderation` | `bool` | Required | - |
| `can_impersonate` | `bool` | Required | - |
| `like_count` | `int` | Required | - |
| `like_given_count` | `int` | Required | - |
| `topic_count` | `int` | Required | - |
| `flags_given_count` | `int` | Required | - |
| `flags_received_count` | `int` | Required | - |
| `private_topics_count` | `int` | Required | - |
| `can_delete_all_posts` | `bool` | Required | - |
| `can_be_deleted` | `bool` | Optional | - |
| `can_be_anonymized` | `bool` | Required | - |
| `can_be_merged` | `bool` | Required | - |
| `full_suspend_reason` | `str` | Required | - |
| `latest_export` | `Any` | Optional | - |
| `full_silence_reason` | `str` | Optional | - |
| `silence_reason` | `str` | Optional | - |
| `post_edits_count` | `int` | Optional | - |
| `primary_group_id` | `int` | Required | - |
| `badge_count` | `int` | Required | - |
| `warnings_received_count` | `int` | Required | - |
| `bounce_score` | `int` | Required | - |
| `reset_bounce_score_after` | `str` | Required | - |
| `can_view_action_logs` | `bool` | Required | - |
| `can_disable_second_factor` | `bool` | Required | - |
| `can_delete_sso_record` | `bool` | Required | - |
| `api_key_count` | `int` | Required | - |
| `similar_users_count` | `int` | Optional | - |
| `single_sign_on_record` | `str` | Required | - |
| `approved_by` | [`ApprovedBy`](../../doc/models/approved-by.md) | Required | - |
| `suspended_by` | `str` | Required | - |
| `silenced_by` | `str` | Required | - |
| `penalty_counts` | [`PenaltyCounts`](../../doc/models/penalty-counts.md) | Optional | - |
| `next_penalty` | `str` | Optional | - |
| `tl_3_requirements` | [`Tl3Requirements`](../../doc/models/tl-3-requirements.md) | Optional | - |
| `groups` | [`List[Group10]`](../../doc/models/group-10.md) | Required | - |
| `external_ids` | `Any` | Required | - |
| `include_ip` | `bool` | Required | - |
| `upcoming_changes_stats` | [`List[UpcomingChangesStat]`](../../doc/models/upcoming-changes-stat.md) | Optional | - |

## Example

```python
import jsonpickle

from discourse.models.admin_users_json_response import AdminUsersJsonResponse
from discourse.models.approved_by import ApprovedBy
from discourse.models.group_10 import Group10

admin_users_json_response = AdminUsersJsonResponse(
    id=0,
    username='username0',
    name='name0',
    avatar_template='avatar_template0',
    active=False,
    admin=False,
    moderator=False,
    last_seen_at='last_seen_at6',
    last_emailed_at='last_emailed_at2',
    created_at='created_at8',
    last_seen_age=48.3,
    last_emailed_age=217.32,
    created_at_age=114.58,
    trust_level=240,
    manual_locked_trust_level='manual_locked_trust_level2',
    title='title6',
    time_read=204,
    staged=False,
    days_visited=20,
    posts_read_count=112,
    topics_entered=14,
    post_count=228,
    can_send_activation_email=False,
    can_activate=False,
    can_deactivate=False,
    ip_address='ip_address0',
    registration_ip_address='registration_ip_address6',
    can_grant_admin=False,
    can_revoke_admin=False,
    can_grant_moderation=False,
    can_revoke_moderation=False,
    can_impersonate=False,
    like_count=254,
    like_given_count=148,
    topic_count=156,
    flags_given_count=96,
    flags_received_count=126,
    private_topics_count=64,
    can_delete_all_posts=False,
    can_be_anonymized=False,
    can_be_merged=False,
    full_suspend_reason='full_suspend_reason2',
    primary_group_id=12,
    badge_count=82,
    warnings_received_count=238,
    bounce_score=66,
    reset_bounce_score_after='reset_bounce_score_after6',
    can_view_action_logs=False,
    can_disable_second_factor=False,
    can_delete_sso_record=False,
    api_key_count=34,
    single_sign_on_record='single_sign_on_record0',
    approved_by=ApprovedBy(
        id=188,
        username='username6',
        name='name4',
        avatar_template='avatar_template6'
    ),
    suspended_by='suspended_by4',
    silenced_by='silenced_by4',
    groups=[
        Group10(
            id=152,
            automatic=False,
            name='name6',
            display_name='display_name6',
            user_count=248,
            mentionable_level=236,
            messageable_level=92,
            visibility_level=196,
            primary_group=False,
            title='title2',
            grant_trust_level='grant_trust_level8',
            incoming_email='incoming_email6',
            has_messages=False,
            flair_url='flair_url6',
            flair_bg_color='flair_bg_color0',
            flair_color='flair_color0',
            bio_raw='bio_raw8',
            bio_cooked='bio_cooked2',
            bio_excerpt='bio_excerpt0',
            public_admission=False,
            public_exit=False,
            allow_membership_requests=False,
            full_name='full_name2',
            default_notification_level=112,
            membership_request_template='membership_request_template2',
            members_visibility_level=0,
            can_see_members=False,
            can_admin_group=False,
            publish_read_state=False,
            flair_group_id=202
        )
    ],
    external_ids=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    include_ip=False,
    associated_accounts=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    can_change_trust_level=False,
    can_be_deleted=False,
    latest_export=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    full_silence_reason='full_silence_reason6'
)
```

