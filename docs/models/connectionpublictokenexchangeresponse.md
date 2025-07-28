# ConnectionPublicTokenExchangeResponse


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `access_token`                                                                      | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The access token associated with the connection data is being requested for         |
| `connection_id`                                                                     | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | The Deck Connection ID for the connection associated with the returned access token |
| `fields`                                                                            | List[[models.LinkConnectRequestField](../models/linkconnectrequestfield.md)]        | :heavy_check_mark:                                                                  | List of non-sensitive values provided from the Link session by the user             |