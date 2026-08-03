
# Notification Types

## Structure

`NotificationTypes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mentioned` | `int` | Required | - |
| `replied` | `int` | Required | - |
| `quoted` | `int` | Required | - |
| `edited` | `int` | Required | - |
| `liked` | `int` | Required | - |
| `private_message` | `int` | Required | - |
| `invited_to_private_message` | `int` | Required | - |
| `invitee_accepted` | `int` | Required | - |
| `posted` | `int` | Required | - |
| `watching_category_or_tag` | `int` | Required | - |
| `new_features` | `int` | Optional | - |
| `admin_problems` | `int` | Optional | - |
| `moved_post` | `int` | Required | - |
| `linked` | `int` | Required | - |
| `granted_badge` | `int` | Required | - |
| `invited_to_topic` | `int` | Required | - |
| `custom` | `int` | Required | - |
| `group_mentioned` | `int` | Required | - |
| `group_message_summary` | `int` | Required | - |
| `watching_first_post` | `int` | Required | - |
| `topic_reminder` | `int` | Required | - |
| `liked_consolidated` | `int` | Required | - |
| `linked_consolidated` | `int` | Required | - |
| `post_approved` | `int` | Required | - |
| `code_review_commit_approved` | `int` | Required | - |
| `membership_request_accepted` | `int` | Required | - |
| `membership_request_consolidated` | `int` | Required | - |
| `bookmark_reminder` | `int` | Required | - |
| `reaction` | `int` | Required | - |
| `votes_released` | `int` | Required | - |
| `event_reminder` | `int` | Required | - |
| `event_invitation` | `int` | Required | - |
| `chat_mention` | `int` | Required | - |
| `chat_message` | `int` | Required | - |
| `chat_invitation` | `int` | Required | - |
| `chat_group_mention` | `int` | Required | - |
| `chat_quoted` | `int` | Optional | - |
| `chat_watched_thread` | `int` | Optional | - |
| `upcoming_change_available` | `int` | Optional | - |
| `upcoming_change_automatically_promoted` | `int` | Optional | - |
| `assigned` | `int` | Optional | - |
| `question_answer_user_commented` | `int` | Optional | - |
| `following` | `int` | Optional | - |
| `following_created_topic` | `int` | Optional | - |
| `following_replied` | `int` | Optional | - |
| `circles_activity` | `int` | Optional | - |
| `boost` | `int` | Optional | - |
| `suggested_edit_created` | `int` | Optional | - |
| `suggested_edit_accepted` | `int` | Optional | - |

## Example

```python
from discourseapidocumentation.models.notification_types import NotificationTypes

notification_types = NotificationTypes(
    mentioned=10,
    replied=148,
    quoted=16,
    edited=82,
    liked=92,
    private_message=206,
    invited_to_private_message=86,
    invitee_accepted=52,
    posted=254,
    watching_category_or_tag=26,
    moved_post=192,
    linked=214,
    granted_badge=110,
    invited_to_topic=200,
    custom=104,
    group_mentioned=70,
    group_message_summary=72,
    watching_first_post=92,
    topic_reminder=128,
    liked_consolidated=110,
    linked_consolidated=94,
    post_approved=8,
    code_review_commit_approved=90,
    membership_request_accepted=54,
    membership_request_consolidated=38,
    bookmark_reminder=230,
    reaction=190,
    votes_released=170,
    event_reminder=38,
    event_invitation=142,
    chat_mention=90,
    chat_message=52,
    chat_invitation=182,
    chat_group_mention=62,
    new_features=44,
    admin_problems=196,
    chat_quoted=4,
    chat_watched_thread=54,
    upcoming_change_available=186
)
```

