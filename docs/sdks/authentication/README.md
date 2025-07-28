# Authentication
(*links.authentication*)

## Overview

### Available Operations

* [get_mfa_question](#get_mfa_question) - Get the security question
* [answer_mfa](#answer_mfa) - Provide MFA code

## get_mfa_question

Call this endpoint when receiving the connection status MfaQuestion, to get the text of the MFA security question

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/link/authentication/mfa/get" method="post" path="/link/authentication/mfa/get" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    res = ds_client.links.authentication.get_mfa_question()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.LinkTokenRequestResponse](../../models/linktokenrequestresponse.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.SecurityQuestionResponse](../../models/securityquestionresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |

## answer_mfa

Call this endpoint to send your MFA code, when receiving MfaCodeRequired or MfaCodeInvalid status from webhook

### Example Usage

<!-- UsageSnippet language="python" operationID="post_/link/authentication/mfa/answer" method="post" path="/link/authentication/mfa/answer" -->
```python
from deck_sdk import DeckSDK, models
import os


with DeckSDK(
    security=models.Security(
        client_id=os.getenv("DECKSDK_CLIENT_ID", ""),
        secret=os.getenv("DECKSDK_SECRET", ""),
    ),
) as ds_client:

    ds_client.links.authentication.answer_mfa()

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [models.SecurityQuestionAnswerSaveRequest](../../models/securityquestionanswersaverequest.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessageResponse | 400                         | application/json            |
| errors.ErrorMessageResponse | 400                         | text/json                   |
| errors.APIError             | 4XX, 5XX                    | \*/\*                       |