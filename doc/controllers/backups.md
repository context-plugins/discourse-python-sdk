# Backups

```python
backups_api = client.backups
```

## Class Name

`BackupsApi`

## Methods

* [Get Backups](../../doc/controllers/backups.md#get-backups)
* [Create Backup](../../doc/controllers/backups.md#create-backup)
* [Send Download Backup Email](../../doc/controllers/backups.md#send-download-backup-email)
* [Download Backup](../../doc/controllers/backups.md#download-backup)


# Get Backups

```python
def get_backups(self)
```

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[AdminBackupsJsonResponse]`](../../doc/models/admin-backups-json-response.md).

## Example Usage

```python
result = backups_api.get_backups()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Backup

```python
def create_backup(self,
                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AdminBackupsJsonRequest`](../../doc/models/admin-backups-json-request.md) | Body, Optional | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdminBackupsJsonResponse1`](../../doc/models/admin-backups-json-response-1.md).

## Example Usage

```python
result = backups_api.create_backup()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Download Backup Email

```python
def send_download_backup_email(self,
                              filename)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filename` | `str` | Template, Required | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
filename = 'filename2'

result = backups_api.send_download_backup_email(filename)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Download Backup

```python
def download_backup(self,
                   filename,
                   token)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filename` | `str` | Template, Required | - |
| `token` | `str` | Query, Required | - |

## Response Type

**200**: success response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
filename = 'filename2'

token = 'token6'

result = backups_api.download_backup(
    filename,
    token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

