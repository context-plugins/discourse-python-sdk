
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| default_host | `str` | *Default*: `"discourse.example.com"` |
| environment | [`Environment`](../README.md#environments) | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT", "GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](../doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](../doc/logging-configuration.md) | The SDK logging configuration for API calls |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
import logging

from discourseapidocumentation.configuration import Environment
from discourseapidocumentation.discourseapidocumentation_client import DiscourseapidocumentationClient
from discourseapidocumentation.logging.configuration.api_logging_configuration import LoggingConfiguration
from discourseapidocumentation.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from discourseapidocumentation.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration

client = DiscourseapidocumentationClient(
    environment=Environment.PRODUCTION,
    default_host='discourse.example.com',
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)
```

## Environment-Based Client Initialization

```python
from discourseapidocumentation.discourseapidocumentation_client import DiscourseapidocumentationClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = DiscourseapidocumentationClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## Discourse API Documentation Client

The gateway for the SDK. This class acts as a factory for the Apis and also holds the configuration of the SDK.

## Apis

| Name | Description |
|  --- | --- |
| discourse_calendar_events | Gets DiscourseCalendarEventsApi |
| backups | Gets BackupsApi |
| badges | Gets BadgesApi |
| categories | Gets CategoriesApi |
| groups | Gets GroupsApi |
| invites | Gets InvitesApi |
| notifications | Gets NotificationsApi |
| posts | Gets PostsApi |
| private_messages | Gets PrivateMessagesApi |
| search | Gets SearchApi |
| site | Gets SiteApi |
| tags | Gets TagsApi |
| topics | Gets TopicsApi |
| uploads | Gets UploadsApi |
| users | Gets UsersApi |

