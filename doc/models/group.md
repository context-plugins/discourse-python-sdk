
# Group

## Structure

`Group`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `full_name` | `str` | Optional | - |
| `bio_raw` | `str` | Optional | About Group |
| `usernames` | `str` | Optional | comma,separated |
| `owner_usernames` | `str` | Optional | comma,separated |
| `automatic_membership_email_domains` | `str` | Optional | pipe\|separated |
| `visibility_level` | `int` | Optional | - |
| `primary_group` | `bool` | Optional | - |
| `flair_icon` | `str` | Optional | - |
| `flair_upload_id` | `int` | Optional | - |
| `flair_bg_color` | `str` | Optional | - |
| `public_admission` | `bool` | Optional | - |
| `public_exit` | `bool` | Optional | - |
| `default_notification_level` | `int` | Optional | - |
| `muted_category_ids` | `List[int]` | Optional | - |
| `regular_category_ids` | `List[int]` | Optional | - |
| `watching_category_ids` | `List[int]` | Optional | - |
| `tracking_category_ids` | `List[int]` | Optional | - |
| `watching_first_post_category_ids` | `List[int]` | Optional | - |

## Example

```python
from discourseapidocumentation.models.group import Group

group = Group(
    name='name8',
    full_name='full_name4',
    bio_raw='bio_raw0',
    usernames='usernames0',
    owner_usernames='owner_usernames8',
    automatic_membership_email_domains='automatic_membership_email_domains2'
)
```

