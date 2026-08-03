# Users

```python
users_api = client.users
```

## Class Name

`UsersApi`

## Methods

* [Create User](../../doc/controllers/users.md#create-user)
* [Get User](../../doc/controllers/users.md#get-user)
* [Update User](../../doc/controllers/users.md#update-user)
* [Get User External Id](../../doc/controllers/users.md#get-user-external-id)
* [Get User Identiy Provider External Id](../../doc/controllers/users.md#get-user-identiy-provider-external-id)
* [Update Avatar](../../doc/controllers/users.md#update-avatar)
* [Update Email](../../doc/controllers/users.md#update-email)
* [Update Username](../../doc/controllers/users.md#update-username)
* [List Users Public](../../doc/controllers/users.md#list-users-public)
* [Admin Get User](../../doc/controllers/users.md#admin-get-user)
* [Delete User](../../doc/controllers/users.md#delete-user)
* [Activate User](../../doc/controllers/users.md#activate-user)
* [Deactivate User](../../doc/controllers/users.md#deactivate-user)
* [Suspend User](../../doc/controllers/users.md#suspend-user)
* [Silence User](../../doc/controllers/users.md#silence-user)
* [Anonymize User](../../doc/controllers/users.md#anonymize-user)
* [Log Out User](../../doc/controllers/users.md#log-out-user)
* [Refresh Gravatar](../../doc/controllers/users.md#refresh-gravatar)
* [Admin List Users](../../doc/controllers/users.md#admin-list-users)
* [Admin List Users Flag](../../doc/controllers/users.md#admin-list-users-flag)
* [List User Actions](../../doc/controllers/users.md#list-user-actions)
* [Send Password Reset Email](../../doc/controllers/users.md#send-password-reset-email)
* [Change Password](../../doc/controllers/users.md#change-password)
* [Get User Emails](../../doc/controllers/users.md#get-user-emails)


# Create User

```python
def create_user(self,
               api_key,
               api_username,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `body` | [`UsersJsonRequest`](../../doc/models/users-json-request.md) | Body, Optional | - |

## Response Type

**200**: user created

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UsersJsonResponse`](../../doc/models/users-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

result = users_api.create_user(
    api_key,
    api_username
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get User

```python
def get_user(self,
            api_key,
            api_username,
            username)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `username` | `str` | Template, Required | - |

## Response Type

**200**: user with primary group response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UJsonResponse`](../../doc/models/u-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

username = 'username0'

result = users_api.get_user(
    api_key,
    api_username,
    username
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update User

```python
def update_user(self,
               api_key,
               api_username,
               username,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `username` | `str` | Template, Required | - |
| `body` | [`UJsonRequest`](../../doc/models/u-json-request.md) | Body, Optional | - |

## Response Type

**200**: user updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UJsonResponse1`](../../doc/models/u-json-response-1.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

username = 'username0'

result = users_api.update_user(
    api_key,
    api_username,
    username
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get User External Id

```python
def get_user_external_id(self,
                        api_key,
                        api_username,
                        external_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `external_id` | `str` | Template, Required | - |

## Response Type

**200**: user response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UByExternalJsonResponse`](../../doc/models/u-by-external-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

external_id = 'external_id6'

result = users_api.get_user_external_id(
    api_key,
    api_username,
    external_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get User Identiy Provider External Id

```python
def get_user_identiy_provider_external_id(self,
                                         api_key,
                                         api_username,
                                         provider,
                                         external_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key` | `str` | Header, Required | - |
| `api_username` | `str` | Header, Required | - |
| `provider` | `str` | Template, Required | Authentication provider name. Can be found in the provider callback<br>URL: `/auth/{provider}/callback` |
| `external_id` | `str` | Template, Required | - |

## Response Type

**200**: user response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UByExternalJsonResponse`](../../doc/models/u-by-external-json-response.md).

## Example Usage

```python
api_key = 'Api-Key6'

api_username = 'Api-Username8'

provider = 'provider8'

external_id = 'external_id6'

result = users_api.get_user_identiy_provider_external_id(
    api_key,
    api_username,
    provider,
    external_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Avatar

```python
def update_avatar(self,
                 username,
                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Template, Required | - |
| `body` | [`UPreferencesAvatarPickJsonRequest`](../../doc/models/u-preferences-avatar-pick-json-request.md) | Body, Optional | - |

## Response Type

**200**: avatar updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UPreferencesAvatarPickJsonResponse`](../../doc/models/u-preferences-avatar-pick-json-response.md).

## Example Usage

```python
username = 'username0'

result = users_api.update_avatar(username)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Email

```python
def update_email(self,
                username,
                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Template, Required | - |
| `body` | [`UPreferencesEmailJsonRequest`](../../doc/models/u-preferences-email-json-request.md) | Body, Optional | - |

## Response Type

**200**: email updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
username = 'username0'

result = users_api.update_email(username)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Username

```python
def update_username(self,
                   username,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Template, Required | - |
| `body` | [`UPreferencesUsernameJsonRequest`](../../doc/models/u-preferences-username-json-request.md) | Body, Optional | - |

## Response Type

**200**: username updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
username = 'username0'

result = users_api.update_username(username)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List Users Public

```python
def list_users_public(self,
                     period,
                     order,
                     asc=None,
                     page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `period` | [`Period1`](../../doc/models/period-1.md) | Query, Required | - |
| `order` | [`Order2`](../../doc/models/order-2.md) | Query, Required | - |
| `asc` | [`Asc`](../../doc/models/asc.md) | Query, Optional | - |
| `page` | `int` | Query, Optional | - |

## Response Type

**200**: directory items response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DirectoryItemsJsonResponse`](../../doc/models/directory-items-json-response.md).

## Example Usage

```python
period = Period1.YEARLY

order = Order2.TOPICS_ENTERED

result = users_api.list_users_public(
    period,
    order
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Admin Get User

```python
def admin_get_user(self,
                  id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminUsersJsonResponse`](../../doc/models/admin-users-json-response.md).

## Example Usage

```python
id = 112

result = users_api.admin_get_user(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete User

```python
def delete_user(self,
               id,
               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |
| `body` | [`AdminUsersJsonRequest`](../../doc/models/admin-users-json-request.md) | Body, Optional | - |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminUsersJsonResponse1`](../../doc/models/admin-users-json-response-1.md).

## Example Usage

```python
id = 112

result = users_api.delete_user(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Activate User

```python
def activate_user(self,
                 id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminUsersActivateJsonResponse`](../../doc/models/admin-users-activate-json-response.md).

## Example Usage

```python
id = 112

result = users_api.activate_user(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Deactivate User

```python
def deactivate_user(self,
                   id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminUsersDeactivateJsonResponse`](../../doc/models/admin-users-deactivate-json-response.md).

## Example Usage

```python
id = 112

result = users_api.deactivate_user(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Suspend User

```python
def suspend_user(self,
                id,
                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |
| `body` | [`AdminUsersSuspendJsonRequest`](../../doc/models/admin-users-suspend-json-request.md) | Body, Optional | - |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminUsersSuspendJsonResponse`](../../doc/models/admin-users-suspend-json-response.md).

## Example Usage

```python
id = 112

body = AdminUsersSuspendJsonRequest(
    suspend_until='2121-02-22',
    reason='reason8',
    post_action='delete'
)

result = users_api.suspend_user(
    id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Silence User

```python
def silence_user(self,
                id,
                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |
| `body` | [`AdminUsersSilenceJsonRequest`](../../doc/models/admin-users-silence-json-request.md) | Body, Optional | - |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminUsersSilenceJsonResponse`](../../doc/models/admin-users-silence-json-response.md).

## Example Usage

```python
id = 112

body = AdminUsersSilenceJsonRequest(
    silenced_till='06/01/2022 08:00:00',
    reason='reason8',
    post_action='delete'
)

result = users_api.silence_user(
    id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Anonymize User

```python
def anonymize_user(self,
                  id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminUsersAnonymizeJsonResponse`](../../doc/models/admin-users-anonymize-json-response.md).

## Example Usage

```python
id = 112

result = users_api.anonymize_user(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Log Out User

```python
def log_out_user(self,
                id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | - |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminUsersLogOutJsonResponse`](../../doc/models/admin-users-log-out-json-response.md).

## Example Usage

```python
id = 112

result = users_api.log_out_user(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Refresh Gravatar

```python
def refresh_gravatar(self,
                    username)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Template, Required | - |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UserAvatarRefreshGravatarJsonResponse`](../../doc/models/user-avatar-refresh-gravatar-json-response.md).

## Example Usage

```python
username = 'username0'

result = users_api.refresh_gravatar(username)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Admin List Users

```python
def admin_list_users(self,
                    order=None,
                    asc=None,
                    page=None,
                    show_emails=None,
                    stats=None,
                    email=None,
                    ip=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order` | [`Order3`](../../doc/models/order-3.md) | Query, Optional | - |
| `asc` | [`Asc`](../../doc/models/asc.md) | Query, Optional | - |
| `page` | `int` | Query, Optional | - |
| `show_emails` | `bool` | Query, Optional | Include user email addresses in response. These requests will<br>be logged in the staff action logs. |
| `stats` | `bool` | Query, Optional | Include user stats information |
| `email` | `str` | Query, Optional | Filter to the user with this email address |
| `ip` | `str` | Query, Optional | Filter to users with this IP address |

## Response Type

**200**: users response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[AdminUsersJsonResponse2]`](../../doc/models/admin-users-json-response-2.md).

## Example Usage

```python
result = users_api.admin_list_users()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Admin List Users Flag

```python
def admin_list_users_flag(self,
                         flag,
                         order=None,
                         asc=None,
                         page=None,
                         show_emails=None,
                         stats=None,
                         email=None,
                         ip=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `flag` | [`Flag`](../../doc/models/flag.md) | Template, Required | - |
| `order` | [`Order3`](../../doc/models/order-3.md) | Query, Optional | - |
| `asc` | [`Asc`](../../doc/models/asc.md) | Query, Optional | - |
| `page` | `int` | Query, Optional | - |
| `show_emails` | `bool` | Query, Optional | Include user email addresses in response. These requests will<br>be logged in the staff action logs. |
| `stats` | `bool` | Query, Optional | Include user stats information |
| `email` | `str` | Query, Optional | Filter to the user with this email address |
| `ip` | `str` | Query, Optional | Filter to users with this IP address |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[AdminUsersListJsonResponse]`](../../doc/models/admin-users-list-json-response.md).

## Example Usage

```python
flag = Flag.STAFF

result = users_api.admin_list_users_flag(flag)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# List User Actions

```python
def list_user_actions(self,
                     offset,
                     username,
                     filter)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | `int` | Query, Required | - |
| `username` | `str` | Query, Required | - |
| `filter` | `str` | Query, Required | - |

## Response Type

**200**: response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UserActionsJsonResponse`](../../doc/models/user-actions-json-response.md).

## Example Usage

```python
offset = 12

username = 'username0'

filter = 'filter4'

result = users_api.list_user_actions(
    offset,
    username,
    filter
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Password Reset Email

```python
def send_password_reset_email(self,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SessionForgotPasswordJsonRequest`](../../doc/models/session-forgot-password-json-request.md) | Body, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SessionForgotPasswordJsonResponse`](../../doc/models/session-forgot-password-json-response.md).

## Example Usage

```python
result = users_api.send_password_reset_email()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Change Password

```python
def change_password(self,
                   token,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token` | `str` | Template, Required | - |
| `body` | [`UsersPasswordResetJsonRequest`](../../doc/models/users-password-reset-json-request.md) | Body, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
token = 'token6'

result = users_api.change_password(token)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get User Emails

```python
def get_user_emails(self,
                   username)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Template, Required | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UEmailsJsonResponse`](../../doc/models/u-emails-json-response.md).

## Example Usage

```python
username = 'username0'

result = users_api.get_user_emails(username)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

