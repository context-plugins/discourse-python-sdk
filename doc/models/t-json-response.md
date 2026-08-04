
# T Json Response

## Structure

`TJsonResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `post_stream` | [`PostStream1`](../../doc/models/post-stream-1.md) | Required | - |
| `timeline_lookup` | `List[Any]` | Required | - |
| `suggested_topics` | [`List[SuggestedTopic]`](../../doc/models/suggested-topic.md) | Required | - |
| `tags` | [`List[Tag]`](../../doc/models/tag.md) | Required | - |
| `tags_descriptions` | `Any` | Required | - |
| `id` | `int` | Required | - |
| `title` | `str` | Required | - |
| `fancy_title` | `str` | Required | - |
| `posts_count` | `int` | Required | - |
| `created_at` | `str` | Required | - |
| `views` | `int` | Required | - |
| `reply_count` | `int` | Required | - |
| `like_count` | `int` | Required | - |
| `last_posted_at` | `str` | Required | - |
| `visible` | `bool` | Required | - |
| `closed` | `bool` | Required | - |
| `archived` | `bool` | Required | - |
| `has_summary` | `bool` | Required | - |
| `archetype` | `str` | Required | - |
| `slug` | `str` | Required | - |
| `category_id` | `int` | Required | - |
| `word_count` | `int` | Required | - |
| `deleted_at` | `str` | Required | - |
| `user_id` | `int` | Required | - |
| `featured_link` | `str` | Required | - |
| `pinned_globally` | `bool` | Required | - |
| `pinned_at` | `str` | Required | - |
| `pinned_until` | `str` | Required | - |
| `image_url` | `str` | Required | - |
| `slow_mode_seconds` | `int` | Required | - |
| `draft` | `str` | Required | - |
| `draft_key` | `str` | Required | - |
| `draft_sequence` | `int` | Required | - |
| `unpinned` | `str` | Required | - |
| `pinned` | `bool` | Required | - |
| `current_post_number` | `int` | Optional | - |
| `highest_post_number` | `int` | Required | - |
| `deleted_by` | `str` | Required | - |
| `has_deleted` | `bool` | Required | - |
| `actions_summary` | [`List[ActionsSummary8]`](../../doc/models/actions-summary-8.md) | Required | - |
| `chunk_size` | `int` | Required | - |
| `bookmarked` | `bool` | Required | - |
| `bookmarks` | `List[Any]` | Required | - |
| `topic_timer` | `str` | Required | - |
| `message_bus_last_id` | `int` | Required | - |
| `participant_count` | `int` | Required | - |
| `show_read_indicator` | `bool` | Required | - |
| `thumbnails` | `str` | Required | - |
| `slow_mode_enabled_until` | `str` | Required | - |
| `details` | [`Details`](../../doc/models/details.md) | Required | - |

## Example

```python
import jsonpickle

from discourse.models.actions_summary import ActionsSummary
from discourse.models.actions_summary_8 import ActionsSummary8
from discourse.models.created_by import CreatedBy
from discourse.models.details import Details
from discourse.models.last_poster import LastPoster
from discourse.models.link_count import LinkCount
from discourse.models.participant_1 import Participant1
from discourse.models.post_4 import Post4
from discourse.models.post_stream_1 import PostStream1
from discourse.models.poster_4 import Poster4
from discourse.models.suggested_topic import SuggestedTopic
from discourse.models.t_json_response import TJsonResponse
from discourse.models.tag import Tag
from discourse.models.user import User

t_json_response = TJsonResponse(
    post_stream=PostStream1(
        posts=[
            Post4(
                id=64,
                name='name6',
                username='username6',
                avatar_template='avatar_template6',
                created_at='created_at4',
                cooked='cooked8',
                post_number=216,
                post_type=210,
                updated_at='updated_at2',
                reply_count=154,
                reply_to_post_number='reply_to_post_number2',
                quote_count=78,
                incoming_link_count=6,
                reads=238,
                readers_count=102,
                score=182.76,
                yours=False,
                topic_id=2,
                topic_slug='topic_slug6',
                display_username='display_username6',
                primary_group_name='primary_group_name4',
                flair_name='flair_name0',
                flair_url='flair_url6',
                flair_bg_color='flair_bg_color0',
                flair_color='flair_color0',
                version=36,
                can_edit=False,
                can_delete=False,
                can_recover=False,
                can_wiki=False,
                link_counts=[
                    LinkCount(
                        url='url4',
                        internal=False,
                        reflection=False,
                        title='title6',
                        clicks=220
                    )
                ],
                read=False,
                user_title='user_title0',
                bookmarked=False,
                actions_summary=[
                    ActionsSummary(
                        id=218,
                        can_act=False
                    )
                ],
                moderator=False,
                admin=False,
                staff=False,
                user_id=160,
                hidden=False,
                trust_level=48,
                deleted_at='deleted_at4',
                user_deleted=False,
                edit_reason='edit_reason4',
                can_view_edit_history=False,
                wiki=False,
                reviewable_id=138,
                reviewable_score_count=40,
                reviewable_score_pending_count=190,
                can_see_hidden_post=False
            )
        ],
        stream=[
            jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        ]
    ),
    timeline_lookup=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    suggested_topics=[
        SuggestedTopic(
            id=132,
            title='title4',
            fancy_title='fancy_title8',
            slug='slug2',
            posts_count=14,
            reply_count=222,
            highest_post_number=110,
            image_url='image_url4',
            created_at='created_at6',
            last_posted_at='last_posted_at0',
            bumped=False,
            bumped_at='bumped_at4',
            archetype='archetype4',
            unseen=False,
            pinned=False,
            unpinned='unpinned0',
            excerpt='excerpt0',
            visible=False,
            closed=False,
            archived=False,
            bookmarked='bookmarked8',
            liked='liked0',
            tags=[
                Tag(
                    id=26,
                    name='name0',
                    slug='slug4',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            tags_descriptions=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            like_count=130,
            views=198,
            category_id=130,
            featured_link='featured_link4',
            posters=[
                Poster4(
                    extras='extras2',
                    description='description8',
                    user=User(
                        id=76,
                        username='username0',
                        name='name0',
                        avatar_template='avatar_template0'
                    )
                )
            ]
        )
    ],
    tags=[
        Tag(
            id=26,
            name='name0',
            slug='slug4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    tags_descriptions=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    id=162,
    title='title4',
    fancy_title='fancy_title8',
    posts_count=44,
    created_at='created_at6',
    views=28,
    reply_count=252,
    like_count=160,
    last_posted_at='last_posted_at0',
    visible=False,
    closed=False,
    archived=False,
    has_summary=False,
    archetype='archetype4',
    slug='slug8',
    category_id=100,
    word_count=66,
    deleted_at='deleted_at6',
    user_id=2,
    featured_link='featured_link4',
    pinned_globally=False,
    pinned_at='pinned_at0',
    pinned_until='pinned_until0',
    image_url='image_url4',
    slow_mode_seconds=152,
    draft='draft0',
    draft_key='draft_key8',
    draft_sequence=48,
    unpinned='unpinned0',
    pinned=False,
    highest_post_number=116,
    deleted_by='deleted_by4',
    has_deleted=False,
    actions_summary=[
        ActionsSummary8(
            id=218,
            count=46,
            hidden=False,
            can_act=False
        )
    ],
    chunk_size=160,
    bookmarked=False,
    bookmarks=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ],
    topic_timer='topic_timer8',
    message_bus_last_id=84,
    participant_count=94,
    show_read_indicator=False,
    thumbnails='thumbnails6',
    slow_mode_enabled_until='slow_mode_enabled_until0',
    details=Details(
        can_edit=False,
        notification_level=30,
        can_move_posts=False,
        can_delete=False,
        can_remove_allowed_users=False,
        can_create_post=False,
        can_reply_as_new_topic=False,
        can_convert_topic=False,
        can_review_topic=False,
        can_close_topic=False,
        can_archive_topic=False,
        can_split_merge_topic=False,
        can_edit_staff_notes=False,
        can_toggle_topic_visibility=False,
        can_pin_unpin_topic=False,
        can_moderate_category=False,
        can_remove_self_id=168,
        created_by=CreatedBy(
            id=188,
            username='username8',
            name='name2',
            avatar_template='avatar_template8'
        ),
        last_poster=LastPoster(
            id=254,
            username='username2',
            name='name8',
            avatar_template='avatar_template2'
        ),
        can_invite_to=False,
        can_invite_via_email=False,
        can_flag_topic=False,
        can_banner_topic=False,
        participants=[
            Participant1(
                id=34,
                username='username4',
                name='name4',
                avatar_template='avatar_template6',
                post_count=6,
                primary_group_name='primary_group_name2',
                flair_name='flair_name8',
                flair_url='flair_url4',
                flair_color='flair_color8',
                flair_bg_color='flair_bg_color8',
                admin=False,
                moderator=False,
                trust_level=18,
                flair_group_id=84
            ),
            Participant1(
                id=34,
                username='username4',
                name='name4',
                avatar_template='avatar_template6',
                post_count=6,
                primary_group_name='primary_group_name2',
                flair_name='flair_name8',
                flair_url='flair_url4',
                flair_color='flair_color8',
                flair_bg_color='flair_bg_color8',
                admin=False,
                moderator=False,
                trust_level=18,
                flair_group_id=84
            ),
            Participant1(
                id=34,
                username='username4',
                name='name4',
                avatar_template='avatar_template6',
                post_count=6,
                primary_group_name='primary_group_name2',
                flair_name='flair_name8',
                flair_url='flair_url4',
                flair_color='flair_color8',
                flair_bg_color='flair_bg_color8',
                admin=False,
                moderator=False,
                trust_level=18,
                flair_group_id=84
            )
        ]
    ),
    current_post_number=230
)
```

