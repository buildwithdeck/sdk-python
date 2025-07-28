# Jobs
(*jobs*)

## Overview

Endpoints related to jobs.

### Available Operations

* [submit](#submit) - Send your job requests
* [answer_mfa](#answer_mfa) - Provide MFA code
* [get_document_file](#get_document_file) - Get raw file

## submit

Provide a job code along with its input parameters to execute it

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/jobs/submit" method="post" path="/jobs/submit" -->
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

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.PostJobsSubmitRequest](../../models/postjobssubmitrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.JobResponse](../../models/jobresponse.md)**

### Errors

| Error Type                            | Status Code                           | Content Type                          |
| ------------------------------------- | ------------------------------------- | ------------------------------------- |
| errors.BadRequestJobResponseError     | 400                                   | application/json                      |
| errors.BadRequestJobResponseError     | 400                                   | text/json                             |
| errors.AlreadyRunningJobResponseError | 409                                   | application/json                      |
| errors.AlreadyRunningJobResponseError | 409                                   | text/json                             |
| errors.APIError                       | 4XX, 5XX                              | \*/\*                                 |

## answer_mfa

Call this endpoint to send your MFA code

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/jobs/mfa/answer" method="post" path="/jobs/mfa/answer" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    ds_client.jobs.answer_mfa()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.MfaAnswerRequest](../../models/mfaanswerrequest.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |

## get_document_file

Returns the raw file for the document with the provided document ID

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/jobs/documents/file" method="post" path="/jobs/documents/file" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.jobs.get_document_file()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.RawDocumentRequest](../../models/rawdocumentrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostJobsDocumentsFileResponse](../../models/postjobsdocumentsfileresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |