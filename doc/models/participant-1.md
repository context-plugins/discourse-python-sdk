
# Participant 1

## Structure

`Participant1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `username` | `str` | Required | - |
| `name` | `str` | Required | - |
| `avatar_template` | `str` | Required | - |
| `post_count` | `int` | Required | - |
| `primary_group_name` | `str` | Required | - |
| `flair_name` | `str` | Required | - |
| `flair_url` | `str` | Required | - |
| `flair_color` | `str` | Required | - |
| `flair_bg_color` | `str` | Required | - |
| `flair_group_id` | `int` | Optional | - |
| `admin` | `bool` | Required | - |
| `moderator` | `bool` | Required | - |
| `trust_level` | `int` | Required | - |

## Example

```python
from discourse.models.participant_1 import Participant1

participant_1 = Participant1(
    id=240,
    username='username4',
    name='name6',
    avatar_template='avatar_template4',
    post_count=212,
    primary_group_name='primary_group_name4',
    flair_name='flair_name0',
    flair_url='flair_url6',
    flair_color='flair_color0',
    flair_bg_color='flair_bg_color0',
    admin=False,
    moderator=False,
    trust_level=32,
    flair_group_id=34
)
```

