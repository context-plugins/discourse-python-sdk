
# Groups by Id Json Response

## Structure

`GroupsByIdJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group` | [`Group1`](../../doc/models/group-1.md) | Required | - |
| `extras` | [`Extras`](../../doc/models/extras.md) | Required | - |

## Example

```python
import jsonpickle

from discourseapidocumentation.models.extras import Extras
from discourseapidocumentation.models.group_1 import Group1
from discourseapidocumentation.models.groups_by_id_json_response import GroupsByIdJsonResponse

groups_by_id_json_response = GroupsByIdJsonResponse(
    group=Group1(
        id=38,
        automatic=False,
        name='name8',
        mentionable_level=122,
        messageable_level=234,
        visibility_level=174,
        primary_group=False,
        title='title6',
        grant_trust_level='grant_trust_level0',
        incoming_email='incoming_email2',
        has_messages=False,
        flair_url='flair_url8',
        flair_bg_color='flair_bg_color2',
        flair_color='flair_color8',
        bio_raw='bio_raw0',
        bio_cooked='bio_cooked6',
        bio_excerpt='bio_excerpt2',
        public_admission=False,
        public_exit=False,
        allow_membership_requests=False,
        full_name='full_name4',
        default_notification_level=254,
        membership_request_template='membership_request_template6',
        is_group_user=False,
        members_visibility_level=142,
        can_see_members=False,
        can_admin_group=False,
        publish_read_state=False,
        is_group_owner_display=False,
        mentionable=False,
        messageable=False,
        automatic_membership_email_domains='automatic_membership_email_domains2',
        smtp_server='smtp_server0',
        smtp_port='smtp_port0',
        smtp_ssl_mode=50,
        email_username='email_username6',
        email_password='email_password0',
        message_count=204,
        allow_unknown_sender_topic_replies=False,
        watching_category_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        tracking_category_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        watching_first_post_category_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        regular_category_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        muted_category_ids=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ],
        user_count=122,
        can_edit_group=False,
        smtp_updated_at='smtp_updated_at6',
        smtp_updated_by=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        smtp_enabled=False
    ),
    extras=Extras(
        visible_group_names=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ]
    )
)
```

