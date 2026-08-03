# Private Messages

```python
private_messages_api = client.private_messages
```

## Class Name

`PrivateMessagesApi`

## Methods

* [List User Private Messages](../../doc/controllers/private-messages.md#list-user-private-messages)
* [Get User Sent Private Messages](../../doc/controllers/private-messages.md#get-user-sent-private-messages)


# List User Private Messages

```python
def list_user_private_messages(self,
                              username)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Template, Required | - |

## Response Type

**200**: private messages

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TopicsPrivateMessagesJsonResponse`](../../doc/models/topics-private-messages-json-response.md).

## Example Usage

```python
username = 'username0'

result = private_messages_api.list_user_private_messages(username)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get User Sent Private Messages

```python
def get_user_sent_private_messages(self,
                                  username)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Template, Required | - |

## Response Type

**200**: private messages

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TopicsPrivateMessagesSentJsonResponse`](../../doc/models/topics-private-messages-sent-json-response.md).

## Example Usage

```python
username = 'username0'

result = private_messages_api.get_user_sent_private_messages(username)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

