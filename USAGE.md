<!-- Start SDK Example Usage [usage] -->
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