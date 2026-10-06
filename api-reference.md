# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [DiscourseClient](discourse/client.py)

## Admin

> Source: [Admin](discourse/apis/admin.py)

<details>
<summary><code>def activate_user(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> AdminUsersActivateJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.activate_user(1)
    # TODO: Handle 'response' of type AdminUsersActivateJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.activate_user(1)
    # TODO: Handle 'response' of type AdminUsersActivateJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersActivateJsonResponse](discourse/models/admin_users_activate_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_get_user(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> AdminUsersJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_get_user(1)
    # TODO: Handle 'response' of type AdminUsersJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_get_user(1)
    # TODO: Handle 'response' of type AdminUsersJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersJsonResponse](discourse/models/admin_users_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_list_users(*, order: Order3OrStr | None = None, asc: AscOrStr | None = None, page: int | None = None, show_emails: bool | None = None, stats: bool | None = None, email: str | None = None, ip: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[AdminUsersJsonResponse2]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_list_users()
    # TODO: Handle 'response' of type list[AdminUsersJsonResponse2]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_list_users()
    # TODO: Handle 'response' of type list[AdminUsersJsonResponse2]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order</code> | <code>[Order3OrStr](discourse/models/enums/order3.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>asc</code> | <code>[AscOrStr](discourse/models/enums/asc.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>show_emails</code> | <code>bool \| None</code> | Include user email addresses in response. These requests will<br>be logged in the staff action logs.<br>**Default**: <code>None</code> |
| <code>stats</code> | <code>bool \| None</code> | Include user stats information<br>**Default**: <code>None</code> |
| <code>email</code> | <code>str \| None</code> | Filter to the user with this email address<br>**Default**: <code>None</code> |
| <code>ip</code> | <code>str \| None</code> | Filter to users with this IP address<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[AdminUsersJsonResponse2](discourse/models/admin_users_json_response2.py)&#93;</code> -- users response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_list_users_flag(flag: FlagOrStr, *, order: Order3OrStr | None = None, asc: AscOrStr | None = None, page: int | None = None, show_emails: bool | None = None, stats: bool | None = None, email: str | None = None, ip: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[AdminUsersListJsonResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_list_users_flag(Flag.ACTIVE)
    # TODO: Handle 'response' of type list[AdminUsersListJsonResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_list_users_flag(Flag.ACTIVE)
    # TODO: Handle 'response' of type list[AdminUsersListJsonResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>flag</code> | <code>[FlagOrStr](discourse/models/enums/flag.py)</code> | Value sent with the request. |
| <code>order</code> | <code>[Order3OrStr](discourse/models/enums/order3.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>asc</code> | <code>[AscOrStr](discourse/models/enums/asc.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>show_emails</code> | <code>bool \| None</code> | Include user email addresses in response. These requests will<br>be logged in the staff action logs.<br>**Default**: <code>None</code> |
| <code>stats</code> | <code>bool \| None</code> | Include user stats information<br>**Default**: <code>None</code> |
| <code>email</code> | <code>str \| None</code> | Filter to the user with this email address<br>**Default**: <code>None</code> |
| <code>ip</code> | <code>str \| None</code> | Filter to users with this IP address<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[AdminUsersListJsonResponse](discourse/models/admin_users_list_json_response.py)&#93;</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def anonymize_user(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> AdminUsersAnonymizeJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.anonymize_user(1)
    # TODO: Handle 'response' of type AdminUsersAnonymizeJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.anonymize_user(1)
    # TODO: Handle 'response' of type AdminUsersAnonymizeJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersAnonymizeJsonResponse](discourse/models/admin_users_anonymize_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deactivate_user(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> AdminUsersDeactivateJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.deactivate_user(1)
    # TODO: Handle 'response' of type AdminUsersDeactivateJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.deactivate_user(1)
    # TODO: Handle 'response' of type AdminUsersDeactivateJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersDeactivateJsonResponse](discourse/models/admin_users_deactivate_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_user(id_: int, *, body: AdminUsersJsonRequest | AdminUsersJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminUsersJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.delete_user(1)
    # TODO: Handle 'response' of type AdminUsersJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.delete_user(1)
    # TODO: Handle 'response' of type AdminUsersJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>body</code> | <code>[AdminUsersJsonRequest](discourse/models/admin_users_json_request.py) \| [AdminUsersJsonRequestDict](discourse/models/admin_users_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersJsonResponse1](discourse/models/admin_users_json_response1.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def log_out_user(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> AdminUsersLogOutJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.log_out_user(1)
    # TODO: Handle 'response' of type AdminUsersLogOutJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.log_out_user(1)
    # TODO: Handle 'response' of type AdminUsersLogOutJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersLogOutJsonResponse](discourse/models/admin_users_log_out_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def refresh_gravatar(username: str, *, request_options: RequestOptionsOrDict | None = None) -> UserAvatarRefreshGravatarJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.refresh_gravatar("some example string")
    # TODO: Handle 'response' of type UserAvatarRefreshGravatarJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.refresh_gravatar("some example string")
    # TODO: Handle 'response' of type UserAvatarRefreshGravatarJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UserAvatarRefreshGravatarJsonResponse](discourse/models/user_avatar_refresh_gravatar_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def silence_user(id_: int, *, body: AdminUsersSilenceJsonRequest | AdminUsersSilenceJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminUsersSilenceJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.silence_user(1)
    # TODO: Handle 'response' of type AdminUsersSilenceJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.silence_user(1)
    # TODO: Handle 'response' of type AdminUsersSilenceJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>body</code> | <code>[AdminUsersSilenceJsonRequest](discourse/models/admin_users_silence_json_request.py) \| [AdminUsersSilenceJsonRequestDict](discourse/models/admin_users_silence_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersSilenceJsonResponse](discourse/models/admin_users_silence_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def suspend_user(id_: int, *, body: AdminUsersSuspendJsonRequest | AdminUsersSuspendJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminUsersSuspendJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.suspend_user(1)
    # TODO: Handle 'response' of type AdminUsersSuspendJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.suspend_user(1)
    # TODO: Handle 'response' of type AdminUsersSuspendJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>body</code> | <code>[AdminUsersSuspendJsonRequest](discourse/models/admin_users_suspend_json_request.py) \| [AdminUsersSuspendJsonRequestDict](discourse/models/admin_users_suspend_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersSuspendJsonResponse](discourse/models/admin_users_suspend_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Backups

> Source: [Backups](discourse/apis/backups.py)

<details>
<summary><code>def create_backup(*, body: AdminBackupsJsonRequest | AdminBackupsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminBackupsJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.backups.create_backup()
    # TODO: Handle 'response' of type AdminBackupsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.backups.create_backup()
    # TODO: Handle 'response' of type AdminBackupsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AdminBackupsJsonRequest](discourse/models/admin_backups_json_request.py) \| [AdminBackupsJsonRequestDict](discourse/models/admin_backups_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminBackupsJsonResponse1](discourse/models/admin_backups_json_response1.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_backup(filename: str, token: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.backups.download_backup("some example string", "some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.backups.download_backup("some example string", "some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>filename</code> | <code>str</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_backups(*, request_options: RequestOptionsOrDict | None = None) -> list[AdminBackupsJsonResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.backups.get_backups()
    # TODO: Handle 'response' of type list[AdminBackupsJsonResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.backups.get_backups()
    # TODO: Handle 'response' of type list[AdminBackupsJsonResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[AdminBackupsJsonResponse](discourse/models/admin_backups_json_response.py)&#93;</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def send_download_backup_email(filename: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.backups.send_download_backup_email("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.backups.send_download_backup_email("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>filename</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Badges

> Source: [Badges](discourse/apis/badges.py)

<details>
<summary><code>def admin_list_badges(*, request_options: RequestOptionsOrDict | None = None) -> AdminBadgesJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.badges.admin_list_badges()
    # TODO: Handle 'response' of type AdminBadgesJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.badges.admin_list_badges()
    # TODO: Handle 'response' of type AdminBadgesJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminBadgesJsonResponse](discourse/models/admin_badges_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_badge(*, body: AdminBadgesJsonRequest | AdminBadgesJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminBadgesJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.badges.create_badge()
    # TODO: Handle 'response' of type AdminBadgesJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.badges.create_badge()
    # TODO: Handle 'response' of type AdminBadgesJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AdminBadgesJsonRequest](discourse/models/admin_badges_json_request.py) \| [AdminBadgesJsonRequestDict](discourse/models/admin_badges_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminBadgesJsonResponse1](discourse/models/admin_badges_json_response1.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_badge(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.badges.delete_badge(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.badges.delete_badge(1)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_user_badges(username: str, *, request_options: RequestOptionsOrDict | None = None) -> UserBadgesJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.badges.list_user_badges("some example string")
    # TODO: Handle 'response' of type UserBadgesJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.badges.list_user_badges("some example string")
    # TODO: Handle 'response' of type UserBadgesJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UserBadgesJsonResponse](discourse/models/user_badges_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_badge(id_: int, *, body: AdminBadgesJsonRequest1 | AdminBadgesJsonRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminBadgesJsonResponse2</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.badges.update_badge(1)
    # TODO: Handle 'response' of type AdminBadgesJsonResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.badges.update_badge(1)
    # TODO: Handle 'response' of type AdminBadgesJsonResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>body</code> | <code>[AdminBadgesJsonRequest1](discourse/models/admin_badges_json_request1.py) \| [AdminBadgesJsonRequest1Dict](discourse/models/admin_badges_json_request1.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminBadgesJsonResponse2](discourse/models/admin_badges_json_response2.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Categories

> Source: [Categories](discourse/apis/categories.py)

<details>
<summary><code>def create_category(*, body: CategoriesJsonRequest | CategoriesJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> CategoriesJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.categories.create_category()
    # TODO: Handle 'response' of type CategoriesJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.categories.create_category()
    # TODO: Handle 'response' of type CategoriesJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CategoriesJsonRequest](discourse/models/categories_json_request.py) \| [CategoriesJsonRequestDict](discourse/models/categories_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CategoriesJsonResponse](discourse/models/categories_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_category(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> CShowJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.categories.get_category(1)
    # TODO: Handle 'response' of type CShowJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.categories.get_category(1)
    # TODO: Handle 'response' of type CShowJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CShowJsonResponse](discourse/models/c_show_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_site(*, request_options: RequestOptionsOrDict | None = None) -> SiteJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Can be used to fetch all categories and subcategories

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.categories.get_site()
    # TODO: Handle 'response' of type SiteJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.categories.get_site()
    # TODO: Handle 'response' of type SiteJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SiteJsonResponse](discourse/models/site_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_categories(*, include_subcategories: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> CategoriesJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.categories.list_categories()
    # TODO: Handle 'response' of type CategoriesJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.categories.list_categories()
    # TODO: Handle 'response' of type CategoriesJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>include_subcategories</code> | <code>bool \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CategoriesJsonResponse1](discourse/models/categories_json_response1.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_category_topics(slug: str, id_: int, *, request_options: RequestOptionsOrDict | None = None) -> CJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.categories.list_category_topics("some example string", 1)
    # TODO: Handle 'response' of type CJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.categories.list_category_topics("some example string", 1)
    # TODO: Handle 'response' of type CJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>slug</code> | <code>str</code> | Value sent with the request. |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CJsonResponse](discourse/models/c_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_category(id_: int, *, body: CategoriesJsonRequest1 | CategoriesJsonRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> CategoriesJsonResponse2</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.categories.update_category(1)
    # TODO: Handle 'response' of type CategoriesJsonResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.categories.update_category(1)
    # TODO: Handle 'response' of type CategoriesJsonResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>body</code> | <code>[CategoriesJsonRequest1](discourse/models/categories_json_request1.py) \| [CategoriesJsonRequest1Dict](discourse/models/categories_json_request1.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CategoriesJsonResponse2](discourse/models/categories_json_response2.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DiscourseCalendarEvents

> Source: [DiscourseCalendarEvents](discourse/apis/discourse_calendar_events.py)

<details>
<summary><code>def export_events_ics(*, category_id: int | None = None, include_subcategories: IncludeSubcategoriesOrStr | None = None, attending_user: str | None = None, before: RFC3339DateTime | None = None, after: RFC3339DateTime | None = None, order: OrderOrStr | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.discourse_calendar_events.export_events_ics()
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.discourse_calendar_events.export_events_ics()
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>category_id</code> | <code>int \| None</code> | Filter events by category ID<br>**Default**: <code>None</code> |
| <code>include_subcategories</code> | <code>[IncludeSubcategoriesOrStr](discourse/models/enums/include_subcategories.py) \| None</code> | Include events from subcategories when filtering by category<br>**Default**: <code>None</code> |
| <code>attending_user</code> | <code>str \| None</code> | Filter to events where the specified user (username) has RSVP'd<br>as going<br>**Default**: <code>None</code> |
| <code>before</code> | <code>RFC3339DateTime \| None</code> | Return events starting before this date/time (ISO 8601 format)<br>**Default**: <code>None</code> |
| <code>after</code> | <code>RFC3339DateTime \| None</code> | Return events starting after this date/time (ISO 8601 format)<br>**Default**: <code>None</code> |
| <code>order</code> | <code>[OrderOrStr](discourse/models/enums/order.py) \| None</code> | Sort order for events by start date (default: asc)<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of events to return (default: 200)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_events(*, include_details: IncludeDetailsOrStr | None = None, category_id: int | None = None, include_subcategories: IncludeSubcategoriesOrStr | None = None, post_id: int | None = None, attending_user: str | None = None, before: RFC3339DateTime | None = None, after: RFC3339DateTime | None = None, order: OrderOrStr | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> DiscoursePostEventEventsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.discourse_calendar_events.list_events()
    # TODO: Handle 'response' of type DiscoursePostEventEventsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.discourse_calendar_events.list_events()
    # TODO: Handle 'response' of type DiscoursePostEventEventsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>include_details</code> | <code>[IncludeDetailsOrStr](discourse/models/enums/include_details.py) \| None</code> | Include detailed event information (creator, invitees, stats,<br>etc.)<br>**Default**: <code>None</code> |
| <code>category_id</code> | <code>int \| None</code> | Filter events by category ID<br>**Default**: <code>None</code> |
| <code>include_subcategories</code> | <code>[IncludeSubcategoriesOrStr](discourse/models/enums/include_subcategories.py) \| None</code> | Include events from subcategories when filtering by category<br>**Default**: <code>None</code> |
| <code>post_id</code> | <code>int \| None</code> | Filter to events associated with a specific post ID<br>**Default**: <code>None</code> |
| <code>attending_user</code> | <code>str \| None</code> | Filter to events where the specified user (username) has RSVP'd<br>as going<br>**Default**: <code>None</code> |
| <code>before</code> | <code>RFC3339DateTime \| None</code> | Return events starting before this date/time (ISO 8601 format)<br>**Default**: <code>None</code> |
| <code>after</code> | <code>RFC3339DateTime \| None</code> | Return events starting after this date/time (ISO 8601 format)<br>**Default**: <code>None</code> |
| <code>order</code> | <code>[OrderOrStr](discourse/models/enums/order.py) \| None</code> | Sort order for events by start date (default: asc)<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of events to return (default: 200)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DiscoursePostEventEventsJsonResponse](discourse/models/discourse_post_event_events_json_response.py)</code> -- success response (detailed)

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Groups

> Source: [Groups](discourse/apis/groups.py)

<details>
<summary><code>def add_group_members(id_: int, *, body: GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> GroupsMembersJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.groups.add_group_members(1)
    # TODO: Handle 'response' of type GroupsMembersJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.groups.add_group_members(1)
    # TODO: Handle 'response' of type GroupsMembersJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>body</code> | <code>[GroupsMembersJsonRequest](discourse/models/groups_members_json_request.py) \| [GroupsMembersJsonRequestDict](discourse/models/groups_members_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GroupsMembersJsonResponse1](discourse/models/groups_members_json_response1.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_group(*, body: AdminGroupsJsonRequest | AdminGroupsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminGroupsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.groups.create_group()
    # TODO: Handle 'response' of type AdminGroupsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.groups.create_group()
    # TODO: Handle 'response' of type AdminGroupsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AdminGroupsJsonRequest](discourse/models/admin_groups_json_request.py) \| [AdminGroupsJsonRequestDict](discourse/models/admin_groups_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminGroupsJsonResponse](discourse/models/admin_groups_json_response.py)</code> -- group created

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_group(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> AdminGroupsJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.groups.delete_group(1)
    # TODO: Handle 'response' of type AdminGroupsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.groups.delete_group(1)
    # TODO: Handle 'response' of type AdminGroupsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminGroupsJsonResponse1](discourse/models/admin_groups_json_response1.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_group(name: str, *, request_options: RequestOptionsOrDict | None = None) -> GroupsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.groups.get_group("name")
    # TODO: Handle 'response' of type GroupsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.groups.get_group("name")
    # TODO: Handle 'response' of type GroupsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>name</code> | <code>str</code> | Use group name instead of id |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GroupsJsonResponse](discourse/models/groups_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_group_by_id(id_: str, *, request_options: RequestOptionsOrDict | None = None) -> GroupsByIdJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.groups.get_group_by_id("name")
    # TODO: Handle 'response' of type GroupsByIdJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.groups.get_group_by_id("name")
    # TODO: Handle 'response' of type GroupsByIdJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Use group name instead of id |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GroupsByIdJsonResponse](discourse/models/groups_by_id_json_response.py)</code> -- success response (by id)

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_group_members(name: str, *, request_options: RequestOptionsOrDict | None = None) -> GroupsMembersJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.groups.list_group_members("name")
    # TODO: Handle 'response' of type GroupsMembersJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.groups.list_group_members("name")
    # TODO: Handle 'response' of type GroupsMembersJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>name</code> | <code>str</code> | Use group name instead of id |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GroupsMembersJsonResponse](discourse/models/groups_members_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_groups(*, request_options: RequestOptionsOrDict | None = None) -> GroupsJsonResponse2</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.groups.list_groups()
    # TODO: Handle 'response' of type GroupsJsonResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.groups.list_groups()
    # TODO: Handle 'response' of type GroupsJsonResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GroupsJsonResponse2](discourse/models/groups_json_response2.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_group_members(id_: int, *, body: GroupsMembersJsonRequest | GroupsMembersJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> GroupsMembersJsonResponse2</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.groups.remove_group_members(1)
    # TODO: Handle 'response' of type GroupsMembersJsonResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.groups.remove_group_members(1)
    # TODO: Handle 'response' of type GroupsMembersJsonResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>body</code> | <code>[GroupsMembersJsonRequest](discourse/models/groups_members_json_request.py) \| [GroupsMembersJsonRequestDict](discourse/models/groups_members_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GroupsMembersJsonResponse2](discourse/models/groups_members_json_response2.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_group(id_: int, *, body: GroupsJsonRequest | GroupsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> GroupsJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.groups.update_group(1)
    # TODO: Handle 'response' of type GroupsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.groups.update_group(1)
    # TODO: Handle 'response' of type GroupsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>body</code> | <code>[GroupsJsonRequest](discourse/models/groups_json_request.py) \| [GroupsJsonRequestDict](discourse/models/groups_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GroupsJsonResponse1](discourse/models/groups_json_response1.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Invites

> Source: [Invites](discourse/apis/invites.py)

<details>
<summary><code>def create_invite(api_key: str, api_username: str, *, body: InvitesJsonRequest | InvitesJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> InvitesJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invites.create_invite("some example string", "some example string")
    # TODO: Handle 'response' of type InvitesJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.invites.create_invite("some example string", "some example string")
    # TODO: Handle 'response' of type InvitesJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[InvitesJsonRequest](discourse/models/invites_json_request.py) \| [InvitesJsonRequestDict](discourse/models/invites_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InvitesJsonResponse](discourse/models/invites_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_multiple_invites(api_key: str, api_username: str, *, body: InvitesCreateMultipleJsonRequest | InvitesCreateMultipleJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> InvitesCreateMultipleJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invites.create_multiple_invites("some example string", "some example string")
    # TODO: Handle 'response' of type InvitesCreateMultipleJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.invites.create_multiple_invites("some example string", "some example string")
    # TODO: Handle 'response' of type InvitesCreateMultipleJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[InvitesCreateMultipleJsonRequest](discourse/models/invites_create_multiple_json_request.py) \| [InvitesCreateMultipleJsonRequestDict](discourse/models/invites_create_multiple_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InvitesCreateMultipleJsonResponse](discourse/models/invites_create_multiple_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def invite_group_to_topic(id_: str, api_key: str, api_username: str, *, body: TInviteGroupJsonRequest | TInviteGroupJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> TInviteGroupJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invites.invite_group_to_topic("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type TInviteGroupJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.invites.invite_group_to_topic(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type TInviteGroupJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[TInviteGroupJsonRequest](discourse/models/t_invite_group_json_request.py) \| [TInviteGroupJsonRequestDict](discourse/models/t_invite_group_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TInviteGroupJsonResponse](discourse/models/t_invite_group_json_response.py)</code> -- invites to a PM

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def invite_to_topic(id_: str, api_key: str, api_username: str, *, body: TInviteJsonRequest | TInviteJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> TInviteJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.invites.invite_to_topic("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type TInviteJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.invites.invite_to_topic(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type TInviteJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[TInviteJsonRequest](discourse/models/t_invite_json_request.py) \| [TInviteJsonRequestDict](discourse/models/t_invite_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TInviteJsonResponse](discourse/models/t_invite_json_response.py)</code> -- topic updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Notifications

> Source: [Notifications](discourse/apis/notifications.py)

<details>
<summary><code>def get_notifications(*, request_options: RequestOptionsOrDict | None = None) -> NotificationsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.notifications.get_notifications()
    # TODO: Handle 'response' of type NotificationsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.notifications.get_notifications()
    # TODO: Handle 'response' of type NotificationsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[NotificationsJsonResponse](discourse/models/notifications_json_response.py)</code> -- notifications

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def mark_notifications_as_read(*, body: NotificationsMarkReadJsonRequest | NotificationsMarkReadJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> NotificationsMarkReadJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.notifications.mark_notifications_as_read()
    # TODO: Handle 'response' of type NotificationsMarkReadJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.notifications.mark_notifications_as_read()
    # TODO: Handle 'response' of type NotificationsMarkReadJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[NotificationsMarkReadJsonRequest](discourse/models/notifications_mark_read_json_request.py) \| [NotificationsMarkReadJsonRequestDict](discourse/models/notifications_mark_read_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[NotificationsMarkReadJsonResponse](discourse/models/notifications_mark_read_json_response.py)</code> -- notifications marked read

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Posts

> Source: [Posts](discourse/apis/posts.py)

<details>
<summary><code>def create_topic_post_pm(api_key: str, api_username: str, *, body: PostsJsonRequest | PostsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PostsJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.posts.create_topic_post_pm("some example string", "some example string")
    # TODO: Handle 'response' of type PostsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.posts.create_topic_post_pm("some example string", "some example string")
    # TODO: Handle 'response' of type PostsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[PostsJsonRequest](discourse/models/posts_json_request.py) \| [PostsJsonRequestDict](discourse/models/posts_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PostsJsonResponse1](discourse/models/posts_json_response1.py)</code> -- post created

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_post(id_: int, api_key: str, api_username: str, *, body: PostsJsonRequest2 | PostsJsonRequest2Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.posts.delete_post(1, "some example string", "some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.posts.delete_post(1, "some example string", "some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[PostsJsonRequest2](discourse/models/posts_json_request2.py) \| [PostsJsonRequest2Dict](discourse/models/posts_json_request2.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_post(id_: str, *, request_options: RequestOptionsOrDict | None = None) -> PostsJsonResponse2</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint can be used to get the number of likes on a post using the
`actions_summary` property in the response. `actions_summary` responses
with the id of `2` signify a `like`. If there are no `actions_summary`
items with the id of `2`, that means there are 0 likes. Other ids likely
refer to various different flag types.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.posts.get_post("some example string")
    # TODO: Handle 'response' of type PostsJsonResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.posts.get_post("some example string")
    # TODO: Handle 'response' of type PostsJsonResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PostsJsonResponse2](discourse/models/posts_json_response2.py)</code> -- single reviewable post

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_posts(*, before: int | None = None, request_options: RequestOptionsOrDict | None = None) -> PostsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.posts.list_posts()
    # TODO: Handle 'response' of type PostsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.posts.list_posts()
    # TODO: Handle 'response' of type PostsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>before</code> | <code>int \| None</code> | Load posts with an id lower than this value. Useful for pagination.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PostsJsonResponse](discourse/models/posts_json_response.py)</code> -- latest posts

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def lock_post(id_: str, api_key: str, api_username: str, *, body: PostsLockedJsonRequest | PostsLockedJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PostsLockedJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.posts.lock_post("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type PostsLockedJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.posts.lock_post("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type PostsLockedJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[PostsLockedJsonRequest](discourse/models/posts_locked_json_request.py) \| [PostsLockedJsonRequestDict](discourse/models/posts_locked_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PostsLockedJsonResponse](discourse/models/posts_locked_json_response.py)</code> -- post updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def perform_post_action(api_key: str, api_username: str, *, body: PostActionsJsonRequest | PostActionsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PostActionsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.posts.perform_post_action("some example string", "some example string")
    # TODO: Handle 'response' of type PostActionsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.posts.perform_post_action("some example string", "some example string")
    # TODO: Handle 'response' of type PostActionsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[PostActionsJsonRequest](discourse/models/post_actions_json_request.py) \| [PostActionsJsonRequestDict](discourse/models/post_actions_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PostActionsJsonResponse](discourse/models/post_actions_json_response.py)</code> -- post updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def post_replies(id_: str, *, request_options: RequestOptionsOrDict | None = None) -> list[PostsRepliesJsonResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.posts.post_replies("some example string")
    # TODO: Handle 'response' of type list[PostsRepliesJsonResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.posts.post_replies("some example string")
    # TODO: Handle 'response' of type list[PostsRepliesJsonResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[PostsRepliesJsonResponse](discourse/models/posts_replies_json_response.py)&#93;</code> -- post replies

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_post(id_: str, api_key: str, api_username: str, *, body: PostsJsonRequest1 | PostsJsonRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> PostsJsonResponse3</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.posts.update_post("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type PostsJsonResponse3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.posts.update_post("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type PostsJsonResponse3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[PostsJsonRequest1](discourse/models/posts_json_request1.py) \| [PostsJsonRequest1Dict](discourse/models/posts_json_request1.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PostsJsonResponse3](discourse/models/posts_json_response3.py)</code> -- post updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## PrivateMessages

> Source: [PrivateMessages](discourse/apis/private_messages.py)

<details>
<summary><code>def create_topic_post_pm(api_key: str, api_username: str, *, body: PostsJsonRequest | PostsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PostsJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.private_messages.create_topic_post_pm("some example string", "some example string")
    # TODO: Handle 'response' of type PostsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.private_messages.create_topic_post_pm("some example string", "some example string")
    # TODO: Handle 'response' of type PostsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[PostsJsonRequest](discourse/models/posts_json_request.py) \| [PostsJsonRequestDict](discourse/models/posts_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PostsJsonResponse1](discourse/models/posts_json_response1.py)</code> -- post created

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user_sent_private_messages(username: str, *, request_options: RequestOptionsOrDict | None = None) -> TopicsPrivateMessagesSentJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.private_messages.get_user_sent_private_messages("some example string")
    # TODO: Handle 'response' of type TopicsPrivateMessagesSentJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.private_messages.get_user_sent_private_messages("some example string")
    # TODO: Handle 'response' of type TopicsPrivateMessagesSentJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TopicsPrivateMessagesSentJsonResponse](discourse/models/topics_private_messages_sent_json_response.py)</code> -- private messages

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_user_private_messages(username: str, *, request_options: RequestOptionsOrDict | None = None) -> TopicsPrivateMessagesJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.private_messages.list_user_private_messages("some example string")
    # TODO: Handle 'response' of type TopicsPrivateMessagesJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.private_messages.list_user_private_messages("some example string")
    # TODO: Handle 'response' of type TopicsPrivateMessagesJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TopicsPrivateMessagesJsonResponse](discourse/models/topics_private_messages_json_response.py)</code> -- private messages

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Search

> Source: [Search](discourse/apis/search.py)

<details>
<summary><code>def search(*, q: str | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SearchJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.search.search(
        q="api @blake #support tags:api after:2021-06-04 in:unseen in:open\norder:latest_topic", page=1
    )
    # TODO: Handle 'response' of type SearchJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.search.search(
        q="api @blake #support tags:api after:2021-06-04 in:unseen in:open\norder:latest_topic", page=1
    )
    # TODO: Handle 'response' of type SearchJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>q</code> | <code>str \| None</code> | The query string needs to be url encoded and is made up of the following options:<br>- Search term. This is just a string. Usually it would be the first item in the query.<br>- `@<username>`: Use the `@` followed by the username to specify posts by this user.<br>- `#<category>`: Use the `#` followed by the category slug to search within this category.<br>- `tags:`: `api,solved` or for posts that have all the specified tags `api+solved`.<br>- `before:`: `yyyy-mm-dd`<br>- `after:`: `yyyy-mm-dd`<br>- `order:`: `latest`, `likes`, `views`, `latest_topic`<br>- `assigned:`: username (without `@`)<br>- `in:`: `title`, `likes`, `personal`, `messages`, `seen`, `unseen`, `posted`, `created`, `watching`, `tracking`, `bookmarks`, `assigned`, `unassigned`, `first`, `pinned`, `wiki`<br>- `with:`: `images`<br>- `status:`: `open`, `closed`, `public`, `archived`, `noreplies`, `single_user`, `solved`, `unsolved`<br>- `group:`: group_name or group_id<br>- `group_messages:`: group_name or group_id<br>- `min_posts:`: 1<br>- `max_posts:`: 10<br>- `min_views:`: 1<br>- `max_views:`: 10<br><br>If you are using cURL you can use the `-G` and the `--data-urlencode` flags to encode the query:<br><br>``<br>curl -i -sS -X GET -G "http://localhost:3000/search.json" \<br>--data-urlencode 'q=wordpress @scossar #fun after:2020-01-01'<br>``<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SearchJsonResponse](discourse/models/search_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Site

> Source: [Site](discourse/apis/site.py)

<details>
<summary><code>def get_site(*, request_options: RequestOptionsOrDict | None = None) -> SiteJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Can be used to fetch all categories and subcategories

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.site.get_site()
    # TODO: Handle 'response' of type SiteJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.site.get_site()
    # TODO: Handle 'response' of type SiteJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SiteJsonResponse](discourse/models/site_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_site_basic_info(*, request_options: RequestOptionsOrDict | None = None) -> SiteBasicInfoJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Can be used to fetch basic info about a site

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.site.get_site_basic_info()
    # TODO: Handle 'response' of type SiteBasicInfoJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.site.get_site_basic_info()
    # TODO: Handle 'response' of type SiteBasicInfoJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SiteBasicInfoJsonResponse](discourse/models/site_basic_info_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Tags

> Source: [Tags](discourse/apis/tags.py)

<details>
<summary><code>def create_tag_group(*, body: TagGroupsJsonRequest | TagGroupsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> TagGroupsJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tags.create_tag_group()
    # TODO: Handle 'response' of type TagGroupsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.tags.create_tag_group()
    # TODO: Handle 'response' of type TagGroupsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TagGroupsJsonRequest](discourse/models/tag_groups_json_request.py) \| [TagGroupsJsonRequestDict](discourse/models/tag_groups_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TagGroupsJsonResponse1](discourse/models/tag_groups_json_response1.py)</code> -- tag group created

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_tag(name: str, *, request_options: RequestOptionsOrDict | None = None) -> TagJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tags.get_tag("some example string")
    # TODO: Handle 'response' of type TagJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.tags.get_tag("some example string")
    # TODO: Handle 'response' of type TagJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>name</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TagJsonResponse](discourse/models/tag_json_response.py)</code> -- notifications

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_tag_group(id_: str, *, request_options: RequestOptionsOrDict | None = None) -> TagGroupsJsonResponse2</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tags.get_tag_group("some example string")
    # TODO: Handle 'response' of type TagGroupsJsonResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.tags.get_tag_group("some example string")
    # TODO: Handle 'response' of type TagGroupsJsonResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TagGroupsJsonResponse2](discourse/models/tag_groups_json_response2.py)</code> -- notifications

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_tag_groups(*, request_options: RequestOptionsOrDict | None = None) -> TagGroupsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tags.list_tag_groups()
    # TODO: Handle 'response' of type TagGroupsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.tags.list_tag_groups()
    # TODO: Handle 'response' of type TagGroupsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TagGroupsJsonResponse](discourse/models/tag_groups_json_response.py)</code> -- tags

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_tags(*, request_options: RequestOptionsOrDict | None = None) -> TagsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tags.list_tags()
    # TODO: Handle 'response' of type TagsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.tags.list_tags()
    # TODO: Handle 'response' of type TagsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TagsJsonResponse](discourse/models/tags_json_response.py)</code> -- notifications

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_tag_group(id_: str, *, body: TagGroupsJsonRequest1 | TagGroupsJsonRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None) -> TagGroupsJsonResponse3</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.tags.update_tag_group("some example string")
    # TODO: Handle 'response' of type TagGroupsJsonResponse3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.tags.update_tag_group("some example string")
    # TODO: Handle 'response' of type TagGroupsJsonResponse3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[TagGroupsJsonRequest1](discourse/models/tag_groups_json_request1.py) \| [TagGroupsJsonRequest1Dict](discourse/models/tag_groups_json_request1.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TagGroupsJsonResponse3](discourse/models/tag_groups_json_response3.py)</code> -- Tag group updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Topics

> Source: [Topics](discourse/apis/topics.py)

<details>
<summary><code>def bookmark_topic(id_: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.topics.bookmark_topic("some example string", "some example string", "some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.topics.bookmark_topic("some example string", "some example string", "some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_topic_post_pm(api_key: str, api_username: str, *, body: PostsJsonRequest | PostsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> PostsJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.topics.create_topic_post_pm("some example string", "some example string")
    # TODO: Handle 'response' of type PostsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.topics.create_topic_post_pm("some example string", "some example string")
    # TODO: Handle 'response' of type PostsJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[PostsJsonRequest](discourse/models/posts_json_request.py) \| [PostsJsonRequestDict](discourse/models/posts_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PostsJsonResponse1](discourse/models/posts_json_response1.py)</code> -- post created

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_topic_timer(id_: str, api_key: str, api_username: str, *, body: TTimerJsonRequest | TTimerJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> TTimerJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.topics.create_topic_timer("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type TTimerJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.topics.create_topic_timer(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type TTimerJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[TTimerJsonRequest](discourse/models/t_timer_json_request.py) \| [TTimerJsonRequestDict](discourse/models/t_timer_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TTimerJsonResponse](discourse/models/t_timer_json_response.py)</code> -- topic updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_specific_posts_from_topic(id_: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None) -> TPostsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.topics.get_specific_posts_from_topic(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type TPostsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.topics.get_specific_posts_from_topic(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type TPostsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TPostsJsonResponse](discourse/models/t_posts_json_response.py)</code> -- specific posts

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_topic(id_: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None) -> TJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.topics.get_topic("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type TJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.topics.get_topic("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type TJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TJsonResponse](discourse/models/t_json_response.py)</code> -- specific posts

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_topic_by_external_id(external_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.topics.get_topic_by_external_id("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.topics.get_topic_by_external_id("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>external_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def invite_group_to_topic(id_: str, api_key: str, api_username: str, *, body: TInviteGroupJsonRequest | TInviteGroupJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> TInviteGroupJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.topics.invite_group_to_topic("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type TInviteGroupJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.topics.invite_group_to_topic(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type TInviteGroupJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[TInviteGroupJsonRequest](discourse/models/t_invite_group_json_request.py) \| [TInviteGroupJsonRequestDict](discourse/models/t_invite_group_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TInviteGroupJsonResponse](discourse/models/t_invite_group_json_response.py)</code> -- invites to a PM

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def invite_to_topic(id_: str, api_key: str, api_username: str, *, body: TInviteJsonRequest | TInviteJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> TInviteJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.topics.invite_to_topic("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type TInviteJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.topics.invite_to_topic(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type TInviteJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[TInviteJsonRequest](discourse/models/t_invite_json_request.py) \| [TInviteJsonRequestDict](discourse/models/t_invite_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TInviteJsonResponse](discourse/models/t_invite_json_response.py)</code> -- topic updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_latest_topics(api_key: str, api_username: str, *, order: str | None = None, ascending: str | None = None, per_page: int | None = None, request_options: RequestOptionsOrDict | None = None) -> LatestJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.topics.list_latest_topics("some example string", "some example string")
    # TODO: Handle 'response' of type LatestJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.topics.list_latest_topics("some example string", "some example string")
    # TODO: Handle 'response' of type LatestJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>order</code> | <code>str \| None</code> | Enum: `default`, `created`, `activity`, `views`, `posts`, `category`,<br>`likes`, `op_likes`, `posters`<br>**Default**: <code>None</code> |
| <code>ascending</code> | <code>str \| None</code> | Defaults to `desc`, add `ascending=true` to sort asc<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Maximum number of topics returned, between 1-100<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[LatestJsonResponse](discourse/models/latest_json_response.py)</code> -- topic updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_top_topics(api_key: str, api_username: str, *, period: str | None = None, per_page: int | None = None, request_options: RequestOptionsOrDict | None = None) -> TopJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.topics.list_top_topics("some example string", "some example string")
    # TODO: Handle 'response' of type TopJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.topics.list_top_topics("some example string", "some example string")
    # TODO: Handle 'response' of type TopJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>period</code> | <code>str \| None</code> | Enum: `all`, `yearly`, `quarterly`, `monthly`, `weekly`, `daily`<br>**Default**: <code>None</code> |
| <code>per_page</code> | <code>int \| None</code> | Maximum number of topics returned, between 1-100<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TopJsonResponse](discourse/models/top_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_topic(id_: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.topics.remove_topic("some example string", "some example string", "some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.topics.remove_topic("some example string", "some example string", "some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_notification_level(id_: str, api_key: str, api_username: str, *, body: TNotificationsJsonRequest | TNotificationsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> TNotificationsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.topics.set_notification_level("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type TNotificationsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.topics.set_notification_level(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type TNotificationsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[TNotificationsJsonRequest](discourse/models/t_notifications_json_request.py) \| [TNotificationsJsonRequestDict](discourse/models/t_notifications_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TNotificationsJsonResponse](discourse/models/t_notifications_json_response.py)</code> -- topic updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_topic(id_: str, api_key: str, api_username: str, *, body: TJsonRequest | TJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> TJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.topics.update_topic("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type TJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.topics.update_topic(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type TJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[TJsonRequest](discourse/models/t_json_request.py) \| [TJsonRequestDict](discourse/models/t_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TJsonResponse1](discourse/models/t_json_response1.py)</code> -- topic updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_topic_status(id_: str, api_key: str, api_username: str, *, body: TStatusJsonRequest | TStatusJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> TStatusJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.topics.update_topic_status("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type TStatusJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.topics.update_topic_status(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type TStatusJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[TStatusJsonRequest](discourse/models/t_status_json_request.py) \| [TStatusJsonRequestDict](discourse/models/t_status_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TStatusJsonResponse](discourse/models/t_status_json_response.py)</code> -- topic updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_topic_timestamp(id_: str, api_key: str, api_username: str, *, body: TChangeTimestampJsonRequest | TChangeTimestampJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> TChangeTimestampJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.topics.update_topic_timestamp("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type TChangeTimestampJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.topics.update_topic_timestamp(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type TChangeTimestampJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[TChangeTimestampJsonRequest](discourse/models/t_change_timestamp_json_request.py) \| [TChangeTimestampJsonRequestDict](discourse/models/t_change_timestamp_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TChangeTimestampJsonResponse](discourse/models/t_change_timestamp_json_response.py)</code> -- topic updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Uploads

> Source: [Uploads](discourse/apis/uploads.py)

<details>
<summary><code>def abort_multipart(*, body: UploadsAbortMultipartJsonRequest | UploadsAbortMultipartJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> UploadsAbortMultipartJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint aborts the multipart upload initiated with /create-multipart.
This should be used when cancelling the upload. It does not matter if parts
were already uploaded into the external storage provider.

You must have the correct permissions and CORS settings configured in your
external provider. We support AWS S3 as the default. See:

https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

An external file store must be set up and `enable_direct_s3_uploads` must
be set to true for this endpoint to function.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.uploads.abort_multipart()
    # TODO: Handle 'response' of type UploadsAbortMultipartJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.uploads.abort_multipart()
    # TODO: Handle 'response' of type UploadsAbortMultipartJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UploadsAbortMultipartJsonRequest](discourse/models/uploads_abort_multipart_json_request.py) \| [UploadsAbortMultipartJsonRequestDict](discourse/models/uploads_abort_multipart_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UploadsAbortMultipartJsonResponse](discourse/models/uploads_abort_multipart_json_response.py)</code> -- external upload initialized

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def batch_presign_multipart_parts(*, body: UploadsBatchPresignMultipartPartsJsonRequest | UploadsBatchPresignMultipartPartsJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> UploadsBatchPresignMultipartPartsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Multipart uploads are uploaded in chunks or parts to individual presigned
URLs, similar to the one generated by /generate-presigned-put. The part
numbers provided must be between 1 and 10000. The total number of parts
will depend on the chunk size in bytes that you intend to use to upload
each chunk. For example a 12MB file may have 2 5MB chunks and a final
2MB chunk, for part numbers 1, 2, and 3.

This endpoint will return a presigned URL for each part number provided,
which you can then use to send PUT requests for the binary chunk corresponding
to that part. When the part is uploaded, the provider should return an
ETag for the part, and this should be stored along with the part number,
because this is needed to complete the multipart upload.

You must have the correct permissions and CORS settings configured in your
external provider. We support AWS S3 as the default. See:

https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

An external file store must be set up and `enable_direct_s3_uploads` must
be set to true for this endpoint to function.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.uploads.batch_presign_multipart_parts()
    # TODO: Handle 'response' of type UploadsBatchPresignMultipartPartsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.uploads.batch_presign_multipart_parts()
    # TODO: Handle 'response' of type UploadsBatchPresignMultipartPartsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UploadsBatchPresignMultipartPartsJsonRequest](discourse/models/uploads_batch_presign_multipart_parts_json_request.py) \| [UploadsBatchPresignMultipartPartsJsonRequestDict](discourse/models/uploads_batch_presign_multipart_parts_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UploadsBatchPresignMultipartPartsJsonResponse](discourse/models/uploads_batch_presign_multipart_parts_json_response.py)</code> -- external upload initialized

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def complete_external_upload(*, body: UploadsCompleteExternalUploadJsonRequest | UploadsCompleteExternalUploadJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> UploadsCompleteExternalUploadJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Completes an external upload initialized with /get-presigned-put. The
file will be moved from its temporary location in external storage to
a final destination in the S3 bucket. An Upload record will also be
created in the database in most cases.

If a sha1-checksum was provided in the initial request it will also
be compared with the uploaded file in storage to make sure the same
file was uploaded. The file size will be compared for the same reason.

You must have the correct permissions and CORS settings configured in your
external provider. We support AWS S3 as the default. See:

https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

An external file store must be set up and `enable_direct_s3_uploads` must
be set to true for this endpoint to function.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.uploads.complete_external_upload()
    # TODO: Handle 'response' of type UploadsCompleteExternalUploadJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.uploads.complete_external_upload()
    # TODO: Handle 'response' of type UploadsCompleteExternalUploadJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UploadsCompleteExternalUploadJsonRequest](discourse/models/uploads_complete_external_upload_json_request.py) \| [UploadsCompleteExternalUploadJsonRequestDict](discourse/models/uploads_complete_external_upload_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UploadsCompleteExternalUploadJsonResponse](discourse/models/uploads_complete_external_upload_json_response.py)</code> -- external upload initialized

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def complete_multipart(*, body: UploadsCompleteMultipartJsonRequest | UploadsCompleteMultipartJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> UploadsCompleteMultipartJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Completes the multipart upload in the external store, and copies the
file from its temporary location to its final location in the store.
All of the parts must have been uploaded to the external storage provider.
An Upload record will be completed in most cases once the file is copied
to its final location.

You must have the correct permissions and CORS settings configured in your
external provider. We support AWS S3 as the default. See:

https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

An external file store must be set up and `enable_direct_s3_uploads` must
be set to true for this endpoint to function.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.uploads.complete_multipart()
    # TODO: Handle 'response' of type UploadsCompleteMultipartJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.uploads.complete_multipart()
    # TODO: Handle 'response' of type UploadsCompleteMultipartJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UploadsCompleteMultipartJsonRequest](discourse/models/uploads_complete_multipart_json_request.py) \| [UploadsCompleteMultipartJsonRequestDict](discourse/models/uploads_complete_multipart_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UploadsCompleteMultipartJsonResponse](discourse/models/uploads_complete_multipart_json_response.py)</code> -- external upload initialized

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_multipart_upload(*, body: UploadsCreateMultipartJsonRequest | UploadsCreateMultipartJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> UploadsCreateMultipartJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a multipart upload in the external storage provider, storing
a temporary reference to the external upload similar to /get-presigned-put.

You must have the correct permissions and CORS settings configured in your
external provider. We support AWS S3 as the default. See:

https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

An external file store must be set up and `enable_direct_s3_uploads` must
be set to true for this endpoint to function.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.uploads.create_multipart_upload()
    # TODO: Handle 'response' of type UploadsCreateMultipartJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.uploads.create_multipart_upload()
    # TODO: Handle 'response' of type UploadsCreateMultipartJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UploadsCreateMultipartJsonRequest](discourse/models/uploads_create_multipart_json_request.py) \| [UploadsCreateMultipartJsonRequestDict](discourse/models/uploads_create_multipart_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UploadsCreateMultipartJsonResponse](discourse/models/uploads_create_multipart_json_response.py)</code> -- external upload initialized

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_upload(upload_type: UploadTypeOrStr, *, user_id: int | None = None, synchronous: bool | None = None, file: FileInput | None = None, request_options: RequestOptionsOrDict | None = None) -> UploadsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.uploads.create_upload(UploadType.AVATAR)
    # TODO: Handle 'response' of type UploadsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.uploads.create_upload(UploadType.AVATAR)
    # TODO: Handle 'response' of type UploadsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>upload_type</code> | <code>[UploadTypeOrStr](discourse/models/enums/upload_type.py)</code> | Value sent with the request. |
| <code>user_id</code> | <code>int \| None</code> | required if uploading an avatar<br>**Default**: <code>None</code> |
| <code>synchronous</code> | <code>bool \| None</code> | Use this flag to return an id and url<br>**Default**: <code>None</code> |
| <code>file</code> | <code>FileInput \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UploadsJsonResponse](discourse/models/uploads_json_response.py)</code> -- file uploaded

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_presigned_put(*, body: UploadsGeneratePresignedPutJsonRequest | UploadsGeneratePresignedPutJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> UploadsGeneratePresignedPutJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Direct external uploads bypass the usual method of creating uploads
via the POST /uploads route, and upload directly to an external provider,
which by default is S3. This route begins the process, and will return
a unique identifier for the external upload as well as a presigned URL
which is where the file binary blob should be uploaded to.

Once the upload is complete to the external service, you must call the
POST /complete-external-upload route using the unique identifier returned
by this route, which will create any required Upload record in the Discourse
database and also move file from its temporary location to the final
destination in the external storage service.

You must have the correct permissions and CORS settings configured in your
external provider. We support AWS S3 as the default. See:

https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

An external file store must be set up and `enable_direct_s3_uploads` must
be set to true for this endpoint to function.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.uploads.generate_presigned_put()
    # TODO: Handle 'response' of type UploadsGeneratePresignedPutJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.uploads.generate_presigned_put()
    # TODO: Handle 'response' of type UploadsGeneratePresignedPutJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UploadsGeneratePresignedPutJsonRequest](discourse/models/uploads_generate_presigned_put_json_request.py) \| [UploadsGeneratePresignedPutJsonRequestDict](discourse/models/uploads_generate_presigned_put_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UploadsGeneratePresignedPutJsonResponse](discourse/models/uploads_generate_presigned_put_json_response.py)</code> -- external upload initialized

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Users

> Source: [Users](discourse/apis/users.py)

<details>
<summary><code>def activate_user(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> AdminUsersActivateJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.activate_user(1)
    # TODO: Handle 'response' of type AdminUsersActivateJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.activate_user(1)
    # TODO: Handle 'response' of type AdminUsersActivateJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersActivateJsonResponse](discourse/models/admin_users_activate_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_get_user(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> AdminUsersJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.admin_get_user(1)
    # TODO: Handle 'response' of type AdminUsersJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.admin_get_user(1)
    # TODO: Handle 'response' of type AdminUsersJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersJsonResponse](discourse/models/admin_users_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_list_users(*, order: Order3OrStr | None = None, asc: AscOrStr | None = None, page: int | None = None, show_emails: bool | None = None, stats: bool | None = None, email: str | None = None, ip: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[AdminUsersJsonResponse2]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.admin_list_users()
    # TODO: Handle 'response' of type list[AdminUsersJsonResponse2]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.admin_list_users()
    # TODO: Handle 'response' of type list[AdminUsersJsonResponse2]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order</code> | <code>[Order3OrStr](discourse/models/enums/order3.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>asc</code> | <code>[AscOrStr](discourse/models/enums/asc.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>show_emails</code> | <code>bool \| None</code> | Include user email addresses in response. These requests will<br>be logged in the staff action logs.<br>**Default**: <code>None</code> |
| <code>stats</code> | <code>bool \| None</code> | Include user stats information<br>**Default**: <code>None</code> |
| <code>email</code> | <code>str \| None</code> | Filter to the user with this email address<br>**Default**: <code>None</code> |
| <code>ip</code> | <code>str \| None</code> | Filter to users with this IP address<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[AdminUsersJsonResponse2](discourse/models/admin_users_json_response2.py)&#93;</code> -- users response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_list_users_flag(flag: FlagOrStr, *, order: Order3OrStr | None = None, asc: AscOrStr | None = None, page: int | None = None, show_emails: bool | None = None, stats: bool | None = None, email: str | None = None, ip: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[AdminUsersListJsonResponse]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.admin_list_users_flag(Flag.ACTIVE)
    # TODO: Handle 'response' of type list[AdminUsersListJsonResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.admin_list_users_flag(Flag.ACTIVE)
    # TODO: Handle 'response' of type list[AdminUsersListJsonResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>flag</code> | <code>[FlagOrStr](discourse/models/enums/flag.py)</code> | Value sent with the request. |
| <code>order</code> | <code>[Order3OrStr](discourse/models/enums/order3.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>asc</code> | <code>[AscOrStr](discourse/models/enums/asc.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>show_emails</code> | <code>bool \| None</code> | Include user email addresses in response. These requests will<br>be logged in the staff action logs.<br>**Default**: <code>None</code> |
| <code>stats</code> | <code>bool \| None</code> | Include user stats information<br>**Default**: <code>None</code> |
| <code>email</code> | <code>str \| None</code> | Filter to the user with this email address<br>**Default**: <code>None</code> |
| <code>ip</code> | <code>str \| None</code> | Filter to users with this IP address<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[AdminUsersListJsonResponse](discourse/models/admin_users_list_json_response.py)&#93;</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def anonymize_user(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> AdminUsersAnonymizeJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.anonymize_user(1)
    # TODO: Handle 'response' of type AdminUsersAnonymizeJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.anonymize_user(1)
    # TODO: Handle 'response' of type AdminUsersAnonymizeJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersAnonymizeJsonResponse](discourse/models/admin_users_anonymize_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def change_password(token: str, *, body: UsersPasswordResetJsonRequest | UsersPasswordResetJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.users.change_password("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.users.change_password("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UsersPasswordResetJsonRequest](discourse/models/users_password_reset_json_request.py) \| [UsersPasswordResetJsonRequestDict](discourse/models/users_password_reset_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_user(api_key: str, api_username: str, *, body: UsersJsonRequest | UsersJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> UsersJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.create_user("some example string", "some example string")
    # TODO: Handle 'response' of type UsersJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.create_user("some example string", "some example string")
    # TODO: Handle 'response' of type UsersJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UsersJsonRequest](discourse/models/users_json_request.py) \| [UsersJsonRequestDict](discourse/models/users_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsersJsonResponse](discourse/models/users_json_response.py)</code> -- user created

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deactivate_user(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> AdminUsersDeactivateJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.deactivate_user(1)
    # TODO: Handle 'response' of type AdminUsersDeactivateJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.deactivate_user(1)
    # TODO: Handle 'response' of type AdminUsersDeactivateJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersDeactivateJsonResponse](discourse/models/admin_users_deactivate_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_user(id_: int, *, body: AdminUsersJsonRequest | AdminUsersJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminUsersJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.delete_user(1)
    # TODO: Handle 'response' of type AdminUsersJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.delete_user(1)
    # TODO: Handle 'response' of type AdminUsersJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>body</code> | <code>[AdminUsersJsonRequest](discourse/models/admin_users_json_request.py) \| [AdminUsersJsonRequestDict](discourse/models/admin_users_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersJsonResponse1](discourse/models/admin_users_json_response1.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user(username: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None) -> UJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.get_user("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type UJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.get_user("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type UJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>username</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UJsonResponse](discourse/models/u_json_response.py)</code> -- user with primary group response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user_emails(username: str, *, request_options: RequestOptionsOrDict | None = None) -> UEmailsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.get_user_emails("some example string")
    # TODO: Handle 'response' of type UEmailsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.get_user_emails("some example string")
    # TODO: Handle 'response' of type UEmailsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UEmailsJsonResponse](discourse/models/u_emails_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user_external_id(external_id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None) -> UByExternalJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.get_user_external_id("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type UByExternalJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.get_user_external_id(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type UByExternalJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>external_id</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UByExternalJsonResponse](discourse/models/u_by_external_json_response.py)</code> -- user response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_user_identiy_provider_external_id(provider: str, external_id: str, api_key: str, api_username: str, *, request_options: RequestOptionsOrDict | None = None) -> UByExternalJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.get_user_identiy_provider_external_id(
        "some example string", "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type UByExternalJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.get_user_identiy_provider_external_id(
        "some example string", "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type UByExternalJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>provider</code> | <code>str</code> | Authentication provider name. Can be found in the provider callback<br>URL: `/auth/{provider}/callback` |
| <code>external_id</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UByExternalJsonResponse](discourse/models/u_by_external_json_response.py)</code> -- user response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_user_actions(offset: int, username: str, filter_: str, *, request_options: RequestOptionsOrDict | None = None) -> UserActionsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.list_user_actions(1, "some example string", "some example string")
    # TODO: Handle 'response' of type UserActionsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.list_user_actions(1, "some example string", "some example string")
    # TODO: Handle 'response' of type UserActionsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>offset</code> | <code>int</code> | Value sent with the request. |
| <code>username</code> | <code>str</code> | Value sent with the request. |
| <code>filter_</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UserActionsJsonResponse](discourse/models/user_actions_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_user_badges(username: str, *, request_options: RequestOptionsOrDict | None = None) -> UserBadgesJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.list_user_badges("some example string")
    # TODO: Handle 'response' of type UserBadgesJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.list_user_badges("some example string")
    # TODO: Handle 'response' of type UserBadgesJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UserBadgesJsonResponse](discourse/models/user_badges_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_users_public(period: Period1OrStr, order: Order2OrStr, *, asc: AscOrStr | None = None, page: int | None = None, request_options: RequestOptionsOrDict | None = None) -> DirectoryItemsJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.list_users_public(Period1.DAILY, Order2.LIKES_RECEIVED)
    # TODO: Handle 'response' of type DirectoryItemsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.list_users_public(Period1.DAILY, Order2.LIKES_RECEIVED)
    # TODO: Handle 'response' of type DirectoryItemsJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>period</code> | <code>[Period1OrStr](discourse/models/enums/period1.py)</code> | Value sent with the request. |
| <code>order</code> | <code>[Order2OrStr](discourse/models/enums/order2.py)</code> | Value sent with the request. |
| <code>asc</code> | <code>[AscOrStr](discourse/models/enums/asc.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DirectoryItemsJsonResponse](discourse/models/directory_items_json_response.py)</code> -- directory items response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def log_out_user(id_: int, *, request_options: RequestOptionsOrDict | None = None) -> AdminUsersLogOutJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.log_out_user(1)
    # TODO: Handle 'response' of type AdminUsersLogOutJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.log_out_user(1)
    # TODO: Handle 'response' of type AdminUsersLogOutJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersLogOutJsonResponse](discourse/models/admin_users_log_out_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def refresh_gravatar(username: str, *, request_options: RequestOptionsOrDict | None = None) -> UserAvatarRefreshGravatarJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.refresh_gravatar("some example string")
    # TODO: Handle 'response' of type UserAvatarRefreshGravatarJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.refresh_gravatar("some example string")
    # TODO: Handle 'response' of type UserAvatarRefreshGravatarJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>username</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UserAvatarRefreshGravatarJsonResponse](discourse/models/user_avatar_refresh_gravatar_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def send_password_reset_email(*, body: SessionForgotPasswordJsonRequest | SessionForgotPasswordJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SessionForgotPasswordJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.send_password_reset_email()
    # TODO: Handle 'response' of type SessionForgotPasswordJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.send_password_reset_email()
    # TODO: Handle 'response' of type SessionForgotPasswordJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SessionForgotPasswordJsonRequest](discourse/models/session_forgot_password_json_request.py) \| [SessionForgotPasswordJsonRequestDict](discourse/models/session_forgot_password_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SessionForgotPasswordJsonResponse](discourse/models/session_forgot_password_json_response.py)</code> -- success response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def silence_user(id_: int, *, body: AdminUsersSilenceJsonRequest | AdminUsersSilenceJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminUsersSilenceJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.silence_user(1)
    # TODO: Handle 'response' of type AdminUsersSilenceJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.silence_user(1)
    # TODO: Handle 'response' of type AdminUsersSilenceJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>body</code> | <code>[AdminUsersSilenceJsonRequest](discourse/models/admin_users_silence_json_request.py) \| [AdminUsersSilenceJsonRequestDict](discourse/models/admin_users_silence_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersSilenceJsonResponse](discourse/models/admin_users_silence_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def suspend_user(id_: int, *, body: AdminUsersSuspendJsonRequest | AdminUsersSuspendJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminUsersSuspendJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.suspend_user(1)
    # TODO: Handle 'response' of type AdminUsersSuspendJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.suspend_user(1)
    # TODO: Handle 'response' of type AdminUsersSuspendJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>int</code> | Value sent with the request. |
| <code>body</code> | <code>[AdminUsersSuspendJsonRequest](discourse/models/admin_users_suspend_json_request.py) \| [AdminUsersSuspendJsonRequestDict](discourse/models/admin_users_suspend_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminUsersSuspendJsonResponse](discourse/models/admin_users_suspend_json_response.py)</code> -- response

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_avatar(username: str, *, body: UPreferencesAvatarPickJsonRequest | UPreferencesAvatarPickJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> UPreferencesAvatarPickJsonResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.update_avatar("some example string")
    # TODO: Handle 'response' of type UPreferencesAvatarPickJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.update_avatar("some example string")
    # TODO: Handle 'response' of type UPreferencesAvatarPickJsonResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UPreferencesAvatarPickJsonRequest](discourse/models/u_preferences_avatar_pick_json_request.py) \| [UPreferencesAvatarPickJsonRequestDict](discourse/models/u_preferences_avatar_pick_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UPreferencesAvatarPickJsonResponse](discourse/models/u_preferences_avatar_pick_json_response.py)</code> -- avatar updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_email(username: str, *, body: UPreferencesEmailJsonRequest | UPreferencesEmailJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.users.update_email("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.users.update_email("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UPreferencesEmailJsonRequest](discourse/models/u_preferences_email_json_request.py) \| [UPreferencesEmailJsonRequestDict](discourse/models/u_preferences_email_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_user(username: str, api_key: str, api_username: str, *, body: UJsonRequest | UJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> UJsonResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.update_user("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type UJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.update_user("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type UJsonResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>username</code> | <code>str</code> | Value sent with the request. |
| <code>api_key</code> | <code>str</code> | Value sent with the request. |
| <code>api_username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UJsonRequest](discourse/models/u_json_request.py) \| [UJsonRequestDict](discourse/models/u_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UJsonResponse1](discourse/models/u_json_response1.py)</code> -- user updated

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_username(username: str, *, body: UPreferencesUsernameJsonRequest | UPreferencesUsernameJsonRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.users.update_username("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.users.update_username("some example string")
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>username</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UPreferencesUsernameJsonRequest](discourse/models/u_preferences_username_json_request.py) \| [UPreferencesUsernameJsonRequestDict](discourse/models/u_preferences_username_json_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](discourse/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](discourse/core/exceptions.py)&#91;[RawError](discourse/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

