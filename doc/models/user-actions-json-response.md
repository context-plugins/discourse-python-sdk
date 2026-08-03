
# User Actions Json Response

## Structure

`UserActionsJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_actions` | [`List[UserAction]`](../../doc/models/user-action.md) | Required | - |

## Example

```python
from discourseapidocumentation.models.user_action import UserAction
from discourseapidocumentation.models.user_actions_json_response import UserActionsJsonResponse

user_actions_json_response = UserActionsJsonResponse(
    user_actions=[
        UserAction(
            excerpt='excerpt0',
            action_type=10,
            created_at='created_at6',
            avatar_template='avatar_template8',
            acting_avatar_template='acting_avatar_template0',
            slug='slug2',
            topic_id=168,
            target_user_id=224,
            target_name='target_name2',
            target_username='target_username8',
            post_number=126,
            post_id='post_id2',
            username='username8',
            name='name8',
            user_id=70,
            acting_username='acting_username2',
            acting_name='acting_name2',
            acting_user_id=152,
            title='title4',
            deleted=False,
            hidden='hidden6',
            post_type='post_type0',
            action_code='action_code8',
            category_id=32,
            closed=False,
            archived=False
        )
    ]
)
```

