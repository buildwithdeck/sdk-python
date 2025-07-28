# JobsDocuments
(*jobs_documents*)

## Overview

### Available Operations

* [list](#list) - List documents

## list

Returns a list of documents available for the connection associated with the provided link token

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/jobs/documents/list" method="post" path="/jobs/documents/list" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.jobs_documents.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `job_guid`                                                                | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `access_token_request`                                                    | [Optional[models.AccessTokenRequest]](../../models/accesstokenrequest.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.DocumentListResponse](../../models/documentlistresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |