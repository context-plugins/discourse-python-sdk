
# Tl 3 Requirements

## Structure

`Tl3Requirements`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time_period` | `int` | Required | - |
| `requirements_met` | `bool` | Required | - |
| `requirements_lost` | `bool` | Required | - |
| `trust_level_locked` | `bool` | Required | - |
| `on_grace_period` | `bool` | Required | - |
| `days_visited` | `int` | Required | - |
| `min_days_visited` | `int` | Required | - |
| `num_topics_replied_to` | `int` | Required | - |
| `min_topics_replied_to` | `int` | Required | - |
| `topics_viewed` | `int` | Required | - |
| `min_topics_viewed` | `int` | Required | - |
| `posts_read` | `int` | Required | - |
| `min_posts_read` | `int` | Required | - |
| `topics_viewed_all_time` | `int` | Required | - |
| `min_topics_viewed_all_time` | `int` | Required | - |
| `posts_read_all_time` | `int` | Required | - |
| `min_posts_read_all_time` | `int` | Required | - |
| `num_flagged_posts` | `int` | Required | - |
| `max_flagged_posts` | `int` | Required | - |
| `num_flagged_by_users` | `int` | Required | - |
| `max_flagged_by_users` | `int` | Required | - |
| `num_likes_given` | `int` | Required | - |
| `min_likes_given` | `int` | Required | - |
| `num_likes_received` | `int` | Required | - |
| `min_likes_received` | `int` | Required | - |
| `num_likes_received_days` | `int` | Required | - |
| `min_likes_received_days` | `int` | Required | - |
| `num_likes_received_users` | `int` | Required | - |
| `min_likes_received_users` | `int` | Required | - |
| `penalty_counts` | [`PenaltyCounts1`](../../doc/models/penalty-counts-1.md) | Required | - |

## Example

```python
from discourse.models.penalty_counts_1 import PenaltyCounts1
from discourse.models.tl_3_requirements import Tl3Requirements

tl_3_requirements = Tl3Requirements(
    time_period=82,
    requirements_met=False,
    requirements_lost=False,
    trust_level_locked=False,
    on_grace_period=False,
    days_visited=38,
    min_days_visited=62,
    num_topics_replied_to=56,
    min_topics_replied_to=32,
    topics_viewed=188,
    min_topics_viewed=12,
    posts_read=236,
    min_posts_read=122,
    topics_viewed_all_time=126,
    min_topics_viewed_all_time=212,
    posts_read_all_time=248,
    min_posts_read_all_time=124,
    num_flagged_posts=60,
    max_flagged_posts=170,
    num_flagged_by_users=236,
    max_flagged_by_users=28,
    num_likes_given=58,
    min_likes_given=150,
    num_likes_received=132,
    min_likes_received=174,
    num_likes_received_days=46,
    min_likes_received_days=102,
    num_likes_received_users=200,
    min_likes_received_users=4,
    penalty_counts=PenaltyCounts1(
        silenced=44,
        suspended=238,
        total=2
    )
)
```

