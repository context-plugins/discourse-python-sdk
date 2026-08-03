# Groups

```python
groups_api = client.groups
```

## Class Name

`GroupsApi`

## Methods

* [Create Group](../../doc/controllers/groups.md#create-group)
* [Delete Group](../../doc/controllers/groups.md#delete-group)
* [Get Group](../../doc/controllers/groups.md#get-group)
* [Update Group](../../doc/controllers/groups.md#update-group)
* [Get Group by Id](../../doc/controllers/groups.md#get-group-by-id)
* [List Group Members](../../doc/controllers/groups.md#list-group-members)
* [Add Group Members](../../doc/controllers/groups.md#add-group-members)
* [Remove Group Members](../../doc/controllers/groups.md#remove-group-members)
* [List Groups](../../doc/controllers/groups.md#list-groups)


# Create Group

```python
def create_group(self,
                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AdminGroupsJsonRequest`](../../doc/models/admin-groups-json-request.md) | Body, Optional | - |

## Response Type

**200**: group created

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminGroupsJsonResponse`](../../doc/models/admin-groups-json-response.md).

## Example Usage

```python
result = groups_api.create_group()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Group

```python
def delete_group(self,
                id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminGroupsJsonResponse1`](../../doc/models/admin-groups-json-response-1.md).

## Example Usage

```python
id = 112

result = groups_api.delete_group(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Group

```python
def get_group(self,
             name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Template, Required | Use group name instead of id |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GroupsJsonResponse`](../../doc/models/groups-json-response.md).

## Example Usage

```python
name = 'name'

result = groups_api.get_group(name)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Group

```python
def update_group(self,
                id,
                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |
| `body` | [`GroupsJsonRequest`](../../doc/models/groups-json-request.md) | Body, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GroupsJsonResponse1`](../../doc/models/groups-json-response-1.md).

## Example Usage

```python
id = 112

result = groups_api.update_group(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Group by Id

```python
def get_group_by_id(self,
                   id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | Use group name instead of id |

## Response Type

**200**: success response (by id)

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GroupsByIdJsonResponse`](../../doc/models/groups-by-id-json-response.md).

## Example Usage

```python
id = 'name'

result = groups_api.get_group_by_id(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Group Members

```python
def list_group_members(self,
                      name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Template, Required | Use group name instead of id |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GroupsMembersJsonResponse`](../../doc/models/groups-members-json-response.md).

## Example Usage

```python
name = 'name'

result = groups_api.list_group_members(name)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Add Group Members

```python
def add_group_members(self,
                     id,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |
| `body` | [`GroupsMembersJsonRequest`](../../doc/models/groups-members-json-request.md) | Body, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GroupsMembersJsonResponse1`](../../doc/models/groups-members-json-response-1.md).

## Example Usage

```python
id = 112

body = GroupsMembersJsonRequest(
    usernames='username1,username2'
)

result = groups_api.add_group_members(
    id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Remove Group Members

```python
def remove_group_members(self,
                        id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |
| `body` | [`GroupsMembersJsonRequest`](../../doc/models/groups-members-json-request.md) | Body, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GroupsMembersJsonResponse2`](../../doc/models/groups-members-json-response-2.md).

## Example Usage

```python
id = 112

body = GroupsMembersJsonRequest(
    usernames='username1,username2'
)

result = groups_api.remove_group_members(
    id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Groups

```python
def list_groups(self)
```

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GroupsJsonResponse2`](../../doc/models/groups-json-response-2.md).

## Example Usage

```python
result = groups_api.list_groups()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

