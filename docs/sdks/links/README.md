# Links
(*links*)

## Overview

### Available Operations

* [connect](#connect) - Connect with credentials
* [get_connection_status](#get_connection_status) - Get the status of an attempted connection
* [list_accounts](#list_accounts) - Return the list of accounts found while creating connection

## connect

Sends credential information to a utility data source and attempts to create a connection request asynchronously.

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/link/connect" method="post" path="/link/connect" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.links.connect()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.LinkConnectRequest](../../models/linkconnectrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LinkConnectResponse](../../models/linkconnectresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |

## get_connection_status

Returns the connectivity status about a connection

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/link/connection/status" method="post" path="/link/connection/status" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.links.get_connection_status()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.LinkTokenRequestResponse](../../models/linktokenrequestresponse.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.LinkConnectionStatusResponse](../../models/linkconnectionstatusresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |

## list_accounts

Return the list of accounts found while creating connection

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/link/account/list" method="post" path="/link/account/list" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.links.list_accounts()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.LinkTokenRequestResponse](../../models/linktokenrequestresponse.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.LinkAccountListResponse](../../models/linkaccountlistresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |