# Connection
(*connection*)

## Overview

Manage connections

### Available Operations

* [exchange_public_token](#exchange_public_token) - Exchange public token for an access token
* [get_context](#get_context) - Get connection status details
* [get_accounts](#get_accounts) - Get the connection list of account numbers
* [select_accounts](#select_accounts) - Update the list of accounts to be considered
* [update_auto_refresh](#update_auto_refresh) - Update connection stream config
* [refresh](#refresh) - Request manual refresh
* [destroy](#destroy) - Delete all data related to a connection, losing access to it.

## exchange_public_token

Exchange a Link public_token for an API access_token. Link hands off the public_token client-side via the onSuccess callback once a user has successfully created a connection.

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/connection/public_token/exchange" method="post" path="/connection/public_token/exchange" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.connection.exchange_public_token()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `request`                                                                                           | [models.ConnectionPublicTokenExchangeRequest](../../models/connectionpublictokenexchangerequest.md) | :heavy_check_mark:                                                                                  | The request object to use for the request.                                                          |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.ConnectionPublicTokenExchangeResponse](../../models/connectionpublictokenexchangeresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |

## get_context

Get connection status details

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/connection/context" method="post" path="/connection/context" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.connection.get_context()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AccessTokenRequest](../../models/accesstokenrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConnectionContextResponse](../../models/connectioncontextresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |

## get_accounts

Get the connection list of account numbers

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/connection/accounts" method="post" path="/connection/accounts" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.connection.get_accounts()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AccessTokenRequest](../../models/accesstokenrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetConnectionAccountsResponse](../../models/getconnectionaccountsresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |

## select_accounts

Update the list of accounts to be considered

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/connection/accounts/select" method="post" path="/connection/accounts/select" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    ds_client.connection.select_accounts()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.SelectConnectionAccountsRequest](../../models/selectconnectionaccountsrequest.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |

## update_auto_refresh

You can control which individual connections need to be regularly refreshed or not.

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/connection/auto_refresh/update" method="post" path="/connection/auto_refresh/update" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    ds_client.connection.update_auto_refresh()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.AutoRefreshUpdateRequest](../../models/autorefreshupdaterequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |

## refresh

This will initiate a new session for refreshing the data related to a connection.

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/connection/refresh" method="post" path="/connection/refresh" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    ds_client.connection.refresh()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.RefreshConnectionRequest](../../models/refreshconnectionrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |

## destroy

Delete all data related to a connection, losing access to it.

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/connection/destroy" method="post" path="/connection/destroy" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    ds_client.connection.destroy()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AccessTokenRequest](../../models/accesstokenrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |