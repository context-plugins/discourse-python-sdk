# Notifications

```python
notifications_api = client.notifications
```

## Class Name

`NotificationsApi`

## Methods

* [Get Notifications](../../doc/controllers/notifications.md#get-notifications)
* [Mark Notifications as Read](../../doc/controllers/notifications.md#mark-notifications-as-read)


# Get Notifications

```python
def get_notifications(self)
```

## Response Type

**200**: notifications

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`NotificationsJsonResponse`](../../doc/models/notifications-json-response.md).

## Example Usage

```python
result = notifications_api.get_notifications()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Mark Notifications as Read

```python
def mark_notifications_as_read(self,
                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`NotificationsMarkReadJsonRequest`](../../doc/models/notifications-mark-read-json-request.md) | Body, Optional | - |

## Response Type

**200**: notifications marked read

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`NotificationsMarkReadJsonResponse`](../../doc/models/notifications-mark-read-json-response.md).

## Example Usage

```python
result = notifications_api.mark_notifications_as_read()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

