# Discourse Calendar-Events

```python
discourse_calendar_events_api = client.discourse_calendar_events
```

## Class Name

`DiscourseCalendarEventsApi`

## Methods

* [List Events](../../doc/controllers/discourse-calendar-events.md#list-events)
* [Export Events ICS](../../doc/controllers/discourse-calendar-events.md#export-events-ics)


# List Events

```python
def list_events(self,
               include_details=None,
               category_id=None,
               include_subcategories=None,
               post_id=None,
               attending_user=None,
               before=None,
               after=None,
               order=None,
               limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_details` | [`IncludeDetails`](../../doc/models/include-details.md) | Query, Optional | Include detailed event information (creator, invitees, stats,<br>etc.) |
| `category_id` | `int` | Query, Optional | Filter events by category ID |
| `include_subcategories` | [`IncludeSubcategories`](../../doc/models/include-subcategories.md) | Query, Optional | Include events from subcategories when filtering by category |
| `post_id` | `int` | Query, Optional | Filter to events associated with a specific post ID |
| `attending_user` | `str` | Query, Optional | Filter to events where the specified user (username) has RSVP'd<br>as going |
| `before` | `datetime` | Query, Optional | Return events starting before this date/time (ISO 8601 format) |
| `after` | `datetime` | Query, Optional | Return events starting after this date/time (ISO 8601 format) |
| `order` | [`Order`](../../doc/models/order.md) | Query, Optional | Sort order for events by start date (default: asc) |
| `limit` | `int` | Query, Optional | Maximum number of events to return (default: 200)<br><br>**Constraints**: `>= 1`, `<= 200` |

## Response Type

**200**: success response (detailed)

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DiscoursePostEventEventsJsonResponse`](../../doc/models/discourse-post-event-events-json-response.md).

## Example Usage

```python
result = discourse_calendar_events_api.list_events()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Export Events ICS

```python
def export_events_ics(self,
                     category_id=None,
                     include_subcategories=None,
                     attending_user=None,
                     before=None,
                     after=None,
                     order=None,
                     limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category_id` | `int` | Query, Optional | Filter events by category ID |
| `include_subcategories` | [`IncludeSubcategories`](../../doc/models/include-subcategories.md) | Query, Optional | Include events from subcategories when filtering by category |
| `attending_user` | `str` | Query, Optional | Filter to events where the specified user (username) has RSVP'd<br>as going |
| `before` | `datetime` | Query, Optional | Return events starting before this date/time (ISO 8601 format) |
| `after` | `datetime` | Query, Optional | Return events starting after this date/time (ISO 8601 format) |
| `order` | [`Order`](../../doc/models/order.md) | Query, Optional | Sort order for events by start date (default: asc) |
| `limit` | `int` | Query, Optional | Maximum number of events to return (default: 200)<br><br>**Constraints**: `>= 1`, `<= 200` |

## Response Type

**200**: iCalendar file

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `binary`.

## Example Usage

```python
result = discourse_calendar_events_api.export_events_ics()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

