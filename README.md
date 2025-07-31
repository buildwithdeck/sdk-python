# deck-sdk

Developer-friendly & type-safe Python SDK specifically catered to leverage *deck-sdk* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=deck-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />

<!-- Start Summary [summary] -->
## Summary

Deck API: # Deck API makes it straightforward for users to connect to any portal securely and quickly.

### Welcome! Looking for a quick introduction to our API? Check out the 🚀[Quickstart guide](https://framework.docs.deck.co/docs/setup).

Starting on the sandbox server is easy:

1. Create an account using the [dashboard](https://dashboard.deck.co) to get your client id and sandbox secret
2. Enter your client id and sandbox secret in the Authentication section below
3. Hit the "Try" buttons below for each endpoint.

Happy querying!
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [deck-sdk](#deck-sdk)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from deck-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "deck-sdk",
# ]
# ///

from deck_sdk import DeckSDK

sdk = DeckSDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.jobs.submit(request={
        "job_code": "FetchDocuments",
        "input": {
            "access_token": "access-development-6599f8dd-1a1c-4586-39d1-08ddb97283f7",
            "key1": "value1",
            "someProperty": "someValue",
        },
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from deck_sdk import DeckSDK, models
import os

async def main():

    async with DeckSDK(
        security=models.Security(
            client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
            secret=os.getenv("DECKSDK_SECRET", ""),
        ),
    ) as ds_client:

        res = await ds_client.jobs.submit_async(request={
            "job_code": "FetchDocuments",
            "input": {
                "access_token": "access-development-6599f8dd-1a1c-4586-39d1-08ddb97283f7",
                "key1": "value1",
                "someProperty": "someValue",
            },
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name        | Type   | Scheme  | Environment Variable |
| ----------- | ------ | ------- | -------------------- |
| `client_id` | apiKey | API key | `DECKSDK_CLIENT_ID`  |
| `secret`    | apiKey | API key | `DECKSDK_SECRET`     |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.jobs.submit(request={
        "job_code": "FetchDocuments",
        "input": {
            "access_token": "access-development-6599f8dd-1a1c-4586-39d1-08ddb97283f7",
            "key1": "value1",
            "someProperty": "someValue",
        },
    })

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [connection](docs/sdks/connection/README.md)

* [exchange_public_token](docs/sdks/connection/README.md#exchange_public_token) - Exchange public token for an access token
* [get_context](docs/sdks/connection/README.md#get_context) - Get connection status details
* [get_accounts](docs/sdks/connection/README.md#get_accounts) - Get the connection list of account numbers
* [select_accounts](docs/sdks/connection/README.md#select_accounts) - Update the list of accounts to be considered
* [update_auto_refresh](docs/sdks/connection/README.md#update_auto_refresh) - Update connection stream config
* [refresh](docs/sdks/connection/README.md#refresh) - Request manual refresh
* [destroy](docs/sdks/connection/README.md#destroy) - Delete all data related to a connection, losing access to it.

### [connections](docs/sdks/connections/README.md)

* [invalidate_access_token](docs/sdks/connections/README.md#invalidate_access_token) - Invalidate access_token
* [update_webhook](docs/sdks/connections/README.md#update_webhook) - Update the webhook url for a connection


### [jobs](docs/sdks/jobs/README.md)

* [submit](docs/sdks/jobs/README.md#submit) - Send your job requests
* [answer_mfa](docs/sdks/jobs/README.md#answer_mfa) - Provide MFA code
* [get_document_file](docs/sdks/jobs/README.md#get_document_file) - Get raw file

### [jobs_documents](docs/sdks/jobsdocuments/README.md)

* [list](docs/sdks/jobsdocuments/README.md#list) - List documents

### [link](docs/sdks/link/README.md)

* [create_token](docs/sdks/link/README.md#create_token) - Create a Link Token for running a Link session
* [get_info](docs/sdks/link/README.md#get_info) - Get client information
* [search_sources](docs/sdks/link/README.md#search_sources) - Search sources
* [select_account](docs/sdks/link/README.md#select_account) - Select accounts
* [get_token](docs/sdks/link/README.md#get_token) - Get information about a previously created link_token

### [links](docs/sdks/links/README.md)

* [connect](docs/sdks/links/README.md#connect) - Connect with credentials
* [get_connection_status](docs/sdks/links/README.md#get_connection_status) - Get the status of an attempted connection
* [list_accounts](docs/sdks/links/README.md#list_accounts) - Return the list of accounts found while creating connection

#### [links.authentication](docs/sdks/authentication/README.md)

* [get_mfa_question](docs/sdks/authentication/README.md#get_mfa_question) - Get the security question
* [answer_mfa](docs/sdks/authentication/README.md#answer_mfa) - Provide MFA code

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from deck_sdk import DeckSDK, models
from deck_sdk.utils import BackoffStrategy, RetryConfig
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.jobs.submit(request={
        "job_code": "FetchDocuments",
        "input": {
            "access_token": "access-development-6599f8dd-1a1c-4586-39d1-08ddb97283f7",
            "key1": "value1",
            "someProperty": "someValue",
        },
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from deck_sdk import DeckSDK, models
from deck_sdk.utils import BackoffStrategy, RetryConfig
import os


with DeckSDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.jobs.submit(request={
        "job_code": "FetchDocuments",
        "input": {
            "access_token": "access-development-6599f8dd-1a1c-4586-39d1-08ddb97283f7",
            "key1": "value1",
            "someProperty": "someValue",
        },
    })

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`DeckSDKError`](./src/deck_sdk/errors/decksdkerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from deck_sdk import DeckSDK, errors, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:
    res = None
    try:

        res = ds_client.jobs.submit(request={
            "job_code": "FetchDocuments",
            "input": {
                "access_token": "access-development-6599f8dd-1a1c-4586-39d1-08ddb97283f7",
                "key1": "value1",
                "someProperty": "someValue",
            },
        })

        # Handle response
        print(res)


    except errors.DeckSDKError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.BadRequestJobResponseError):
            print(e.data.error_code)  # models.ErrorCodeEnum
            print(e.data.message)  # Optional[str]
            print(e.data.error_message)  # str
```

### Error Classes
**Primary errors:**
* [`DeckSDKError`](./src/deck_sdk/errors/decksdkerror.py): The base class for HTTP error responses.
  * [`ErrorMessageResponse`](./src/deck_sdk/errors/errormessageresponse.py): Bad Request. Status code `400`. *

<details><summary>Less common errors (7)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`DeckSDKError`](./src/deck_sdk/errors/decksdkerror.py)**:
* [`BadRequestJobResponseError`](./src/deck_sdk/errors/badrequestjobresponseerror.py): Bad Request. Status code `400`. Applicable to 1 of 23 methods.*
* [`AlreadyRunningJobResponseError`](./src/deck_sdk/errors/alreadyrunningjobresponseerror.py): Conflict. Status code `409`. Applicable to 1 of 23 methods.*
* [`ResponseValidationError`](./src/deck_sdk/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                           | Description      |
| --- | -------------------------------- | ---------------- |
| 0   | `https://sandbox.deck.co/api/v1` | Deck Sandbox API |
| 1   | `https://live.deck.co/api/v1`    | Deck API         |

#### Example

```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    server_idx=1,
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.jobs.submit(request={
        "job_code": "FetchDocuments",
        "input": {
            "access_token": "access-development-6599f8dd-1a1c-4586-39d1-08ddb97283f7",
            "key1": "value1",
            "someProperty": "someValue",
        },
    })

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    server_url="https://live.deck.co/api/v1",
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.jobs.submit(request={
        "job_code": "FetchDocuments",
        "input": {
            "access_token": "access-development-6599f8dd-1a1c-4586-39d1-08ddb97283f7",
            "key1": "value1",
            "someProperty": "someValue",
        },
    })

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from deck_sdk import DeckSDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = DeckSDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from deck_sdk import DeckSDK
from deck_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = DeckSDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `DeckSDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from deck_sdk import DeckSDK, models
import os
def main():

    with DeckSDK(
        security=models.Security(
            client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
            secret=os.getenv("DECKSDK_SECRET", ""),
        ),
    ) as ds_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with DeckSDK(
        security=models.Security(
            client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
            secret=os.getenv("DECKSDK_SECRET", ""),
        ),
    ) as ds_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from deck_sdk import DeckSDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = DeckSDK(debug_logger=logging.getLogger("deck_sdk"))
```

You can also enable a default debug logger by setting an environment variable `DECKSDK_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=deck-sdk&utm_campaign=python)
