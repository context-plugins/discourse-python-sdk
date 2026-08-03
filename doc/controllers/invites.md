# Invites

```python
invites_api = client.invites
```

## Class Name

`InvitesApi`

## Methods

* [Create Invite](../../doc/controllers/invites.md#create-invite)
* [Create Multiple Invites](../../doc/controllers/invites.md#create-multiple-invites)


# Create Invite

```python
def create_invite(self,
                 api_key,
                 api_username,
                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `body` | [`InvitesJsonRequest`](../../doc/models/invites-json-request.md) | Body, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvitesJsonResponse`](../../doc/models/invites-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

body = InvitesJsonRequest(
    email='not-a-user-yet@example.com',
    skip_email=False,
    max_redemptions_allowed=5,
    group_ids='42,43',
    group_names='foo,bar'
)

result = invites_api.create_invite(
    api_key,
    api_username,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Multiple Invites

```python
def create_multiple_invites(self,
                           api_key,
                           api_username,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `body` | [`InvitesCreateMultipleJsonRequest`](../../doc/models/invites-create-multiple-json-request.md) | Body, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvitesCreateMultipleJsonResponse`](../../doc/models/invites-create-multiple-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

body = InvitesCreateMultipleJsonRequest(
    email='[\n  "not-a-user-yet-1@example.com",\n  "not-a-user-yet-2@example.com"\n]',
    skip_email=False,
    max_redemptions_allowed=5,
    group_ids='42,43',
    group_names='foo,bar'
)

result = invites_api.create_multiple_invites(
    api_key,
    api_username,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

