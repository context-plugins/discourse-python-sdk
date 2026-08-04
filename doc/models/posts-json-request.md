
# Posts Json Request

## Structure

`PostsJsonRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Optional | Required if creating a new topic or new private message. |
| `raw` | `str` | Required | - |
| `topic_id` | `int` | Optional | Required if creating a new post. |
| `category` | `int` | Optional | Optional if creating a new topic, and ignored if creating<br>a new post. |
| `target_recipients` | `str` | Optional | Required for private message, comma separated. |
| `target_usernames` | `str` | Optional | Deprecated. Use target_recipients instead. |
| `archetype` | `str` | Optional | Required for new private message. |
| `created_at` | `str` | Optional | - |
| `reply_to_post_number` | `int` | Optional | Optional, the post number to reply to inside a topic. |
| `embed_url` | `str` | Optional | Provide a URL from a remote system to associate a forum<br>topic with that URL, typically for using Discourse as a comments<br>system for an external blog. |
| `external_id` | `str` | Optional | Provide an external_id from a remote system to associate<br>a forum topic with that id. |
| `auto_track` | `bool` | Optional | If false, the user will not track the topic. By default,<br>the user will track the topic. |

## Example

```python
from discourse.models.posts_json_request import PostsJsonRequest

posts_json_request = PostsJsonRequest(
    raw='raw8',
    title='title0',
    topic_id=46,
    category=40,
    target_recipients='blake,sam',
    target_usernames='target_usernames8',
    archetype='private_message'
)
```

