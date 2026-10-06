# Discourse SDK

[![Built with APIMatic][apimatic-badge]][apimatic-url] [![License: MIT][license-badge]][license-url] [![Python 3.10+][python-badge]][python-url]

The Discourse SDK for Python provides access to the Discourse REST APIs from Python applications.

> [!TIP]
> **Looking for a specific signature, model, enum, or error type?** This SDK ships a generated
> **[SDK map](sdk-map.md)** -- a lookup index of the SDK's entire Python surface. Consult it before
> scanning the source tree; details under [SDK map](#sdk-map).

This page contains the documentation on how to use Discourse through API calls.

> Note: For any endpoints not listed you can follow the
[reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576)
guide to figure out how to use an API endpoint.

### Request Content-Type

The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`,
`multipart/form-data`, or `application/json`.

### Endpoint Names and Response Content-Type

Most API endpoints provide the same content as their HTML counterparts. For example
the URL `/categories` serves a list of categories, the `/categories.json` API provides the
same information in JSON format.

Instead of sending API requests to `/categories.json` you may also send them to `/categories`
and add an `Accept: application/json` header to the request to get the JSON response.
Sending requests with the `Accept` header is necessary if you want to use URLs
for related endpoints returned by the API, such as pagination URLs.
These URLs are returned without the `.json` prefix so you need to add the header in
order to get the correct response format.

### Authentication

Some endpoints do not require any authentication, pretty much anything else will
require you to be authenticated.

To become authenticated you will need to create an API Key from the admin panel.

Once you have your API Key you can pass it in along with your API Username
as an HTTP header like this:

```
curl -X GET "http://127.0.0.1:3000/admin/users/list/active.json" \
-H "Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19" \
-H "Api-Username: system"
```

and this is how POST requests will look:

```
curl -X POST "http://127.0.0.1:3000/categories" \
-H "Content-Type: multipart/form-data;" \
-H "Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19" \
-H "Api-Username: system" \
-F "name=89853c20-4409-e91a-a8ea-f6cdff96aaaa" \
-F "color=49d9e9" \
-F "text_color=f0fcfd"
```

### Boolean values

If an endpoint accepts a boolean be sure to specify it as a lowercase
`true` or `false` value unless noted otherwise.


---

## Installation

Add the Python SDK to your project from its folder, with whichever package manager your project uses. Give each tool a path containing a slash, such as `../discourse` — a bare folder name is looked up on PyPI instead, and resolves to whatever project holds that name there:

```bash
pip install <path-to-sdk>
```

```bash
uv add <path-to-sdk>
```

```bash
poetry add <path-to-sdk>
```

---

## Quick Start

### Synchronous client

Construct `DiscourseClient` with keyword arguments, and call `close()` when you are done. Every argument is optional; the full list is in the [SDK map](sdk-map.md).

```python
from discourse import DiscourseClient

client = DiscourseClient()

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it -- `with DiscourseClient(...) as client:` closes the pool on exit; see [Best Practices](#best-practices).

`Client` is exported as an alias of `DiscourseClient`, so `from discourse import Client` also works.

The SDK accepts every model-typed input in two interchangeable spellings, both type-checked: the typed model, or a plain dict with the same keys -- the `OrDict` and `Model | ModelDict` unions in the [SDK map](sdk-map.md). Pick whichever suits the call site: the dict form needs no import, while the model form adds a keyword-checked constructor and editor completion.

### Asynchronous client

`AsyncDiscourseClient` mirrors `DiscourseClient` with **identical method names**, and every endpoint method is a coroutine. It takes the same arguments, with some differences -- for example, the transport argument is `custom_async_http_client`.

```python
from asyncio import run

from discourse import AsyncDiscourseClient


async def main() -> None:
    client = AsyncDiscourseClient()
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it -- `async with AsyncDiscourseClient(...) as client:` closes the pool on exit. Only the async spelling is `aclose`, matching httpx2; see [Best Practices](#best-practices).

`AsyncClient` is the exported alias. Each client accepts **only** its own transport argument; passing the other's is a `TypeError` at runtime and an error under mypy.

---

## Usage

Two generated references cover the SDK; each answers a different question:

| Reference | For |
| --- | --- |
| **[API Reference](api-reference.md)** | Usage guidance for a single **parsed** operation: `client.<group>.<operation>(...)` returns the typed payload and raises `ApiError` on any non-2xx, with `.error` the typed error body, or `RawError` for a status the operation does not document. |
| **[Raw API Reference](raw-api-reference.md)** | The same for the **raw** variant: `client.<group>.with_raw_response.<operation>(...)` returns `ApiResult[T, E]` and never raises for an API error. |

Both API references carry every one of the 110 operations, with a sync and an async sample and a parameter table each.

## SDK map

This SDK ships a generated **SDK map** -- [`sdk-map.md`](sdk-map.md) -- a deterministic, lookup-oriented table of contents of the SDK's Python surface, generated by APIMatic alongside this SDK.

Consult the map before scanning or grepping the source: it answers call-level contract questions by lookup, and for anything it does not carry -- model shapes, enum values, an endpoint's route or behavioural prose -- it names the one source file to read. How to read the map itself, including the SDK-wide defaults its rows rely on, is stated at the top of [`sdk-map.md`](sdk-map.md).

## Best Practices

> [!TIP]
> Use a **single `DiscourseClient` instance** for the lifetime of your application and reuse it across
> all requests. Each instance owns its own connection pool, so an instance per request forfeits
> connection reuse and leaks pools that are never closed.

Match the disposal to the client's lifetime: an application-lifetime client is closed once at shutdown with `close()` / `aclose()`; where the lifetime fits a block, `with DiscourseClient() as client:` / `async with AsyncDiscourseClient() as client:` releases it automatically. Both are idempotent, but a closed client is not reusable: the next call raises. The client closes **whatever transport it holds**, including one you supplied via `custom_http_client` / `custom_async_http_client`; if you intend to reuse your own transport across clients, don't hand its lifetime to a `with` block.

**Retries are on by default**: a failed idempotent request — a retryable status or no response at all — is sent again up to three times before the call gives up. Pass `retry_options=0` to turn it off, for instance in a test that stubs an error response; the policy and its defaults are under **Retries** in the SDK map.

## License

This SDK is distributed under the [MIT License][license-url].

---

## Support

Refer to the [API reference](api-reference.md) for detailed information on available operations with code samples.

---

[license-url]: LICENSE
[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg
[apimatic-url]: https://www.apimatic.io
[apimatic-badge]: https://www.apimatic.io/hubfs/Built-with-APIMatic-badge.svg
[python-url]: https://www.python.org/downloads/
[python-badge]: https://img.shields.io/badge/python-3.10%2B-blue.svg
