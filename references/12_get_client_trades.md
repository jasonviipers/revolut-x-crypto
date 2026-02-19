# Get Client Trades (Associated with the Provided API Key)

> `GET /trades/private/{symbol}`

Retrieve the trade history (fills) for the authenticated client. The user context is resolved based on the provided API key.

> **Note:** Rate limit: 1000 requests per minute.

---

## Request

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbol` | string | ✅ Required | Trading pair symbol (e.g., `BTC-USD`). Example: `"BTC-USD"`. |

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `start_date` | integer (int64) | | Start timestamp for the query range in Unix epoch milliseconds. Example: `3318215482991`. If omitted, defaults to 1 week prior to `end_date`. The difference between `start_date` and `end_date` must be <= 1 week. |
| `end_date` | integer (int64) | | End timestamp for the query range in Unix epoch milliseconds. Example: `3318215482991`. If omitted, defaults to the current date if `start_date` is missing. The duration between `start_date` and `end_date` must not exceed 1 week. |
| `cursor` | string | | Pagination cursor obtained from the `metadata.next_cursor` property of the previous response. |
| `limit` | integer | | Maximum number of records to return. Possible values: `1` to `500`. Example: `100`. Default value: `100`. |

### Header Parameters

| Header | Type | Required | Description |
|--------|------|----------|-------------|
| `X-Revx-Timestamp` | integer | ✅ Required | Current timestamp in Unix epoch milliseconds. Used to prevent replay attacks and construct the signature. |
| `X-Revx-Signature` | string | ✅ Required | The Ed25519 signature of the request. |

**Example `X-Revx-Timestamp`:** `1746007718237`

**Example `X-Revx-Signature`:**
```
2h/t5o8w+l5s+fjyFAOn/o7j4u5b7h4e+g4k4c8h7a2p6k0g7j1fiw0i2j3k9r0l3s8m5t6r+q1s+o3v/t4x8v5y+w1r+m2t/k3w/j4y+
```

> **Tip:** See [Authentication headers: Signing a request](#) for details on how to generate the signature.

---

## Response

### 200 – OK

The list of trades.

**Body:** `object`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | array of objects | ✅ Required | List of trade records. |
| `metadata` | object | ✅ Required | Pagination metadata. |

Each trade object in `data` contains:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `tdt` | integer (int64) | ✅ Required | Trade date and time, expressed in Unix epoch milliseconds. |
| `aid` | string | ✅ Required | Crypto asset ID code. Example: `"BTC"`. |
| `anm` | string | ✅ Required | Crypto asset full name. Example: `"Bitcoin"`. |
| `p` | string | ✅ Required | Price in major currency units. For example, for USD, `116243.32` represents 116243.32 dollars. Example: `"116243.32"`. |
| `pc` | string | ✅ Required | Price currency. Example: `"USD"`. |
| `pn` | string | ✅ Required | Price notation. Example: `"NONE"`. |
| `q` | string | ✅ Required | Quantity. Example: `"0.24521000"`. |
| `qc` | string | ✅ Required | Quantity currency. Example: `"BTC"`. |
| `qn` | string | ✅ Required | Quantity notation. Example: `"UNIT"`. |
| `ve` | string | ✅ Required | Venue of execution. Always equals `REVX`. |
| `pdt` | integer (int64) | ✅ Required | Publication date and time, expressed in Unix epoch milliseconds. |
| `vp` | string | ✅ Required | Venue of publication. Always equals `REVX`. |
| `tid` | string | ✅ Required | Transaction identification code. Example: `"5ef9648f658149f7ababedc97a6401f8"`. |

The `metadata` object contains:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `timestamp` | integer (int64) | ✅ Required | Timestamp in Unix epoch milliseconds. |
| `next_cursor` | string | | Cursor used to retrieve the next page of results. To continue paginating, make a new request and pass this value as the `cursor` query parameter. |

**Example Response Body:**
```json
{
  "data": [
    {
      "tdt": 3318215482991,
      "aid": "BTC",
      "anm": "Bitcoin",
      "p": "116243.32",
      "pc": "USD",
      "pn": "NONE",
      "q": "0.24521000",
      "qc": "BTC",
      "qn": "UNIT",
      "ve": "REVX",
      "pdt": 3318215482991,
      "vp": "REVX",
      "tid": "5ef9648f658149f7ababedc97a6401f8"
    }
  ],
  "metadata": {
    "timestamp": 3318215482991,
    "next_cursor": "5Pf8T8ukv3Vd5Nf7MazFfau5dW2f1Pfijfw7t0"
  }
}
```

---

### 400 – Bad Request

**Body:** `object`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `error_id` | string (uuid) | ✅ Required | Unique identifier for this specific error occurrence. |
| `message` | string | ✅ Required | Human-readable description of the error. |
| `timestamp` | integer (int64) | ✅ Required | The time the error occurred in Unix epoch milliseconds. |

---

### 401 – Unauthorized

**Example Response Body:**
```json
{
  "message": "Unauthorized",
  "error_id": "7d85b5e7-d0f0-4696-b7b5-a300d0d03a5e",
  "timestamp": 3318215482991
}
```

---

### 403 – Forbidden

**Example Response Body:**
```json
{
  "message": "Forbidden",
  "error_id": "7d85b5e7-d0f0-4696-b7b5-a300d0d03a5e",
  "timestamp": 3318215482991
}
```

---

### 409 – Conflict

**Example Response Body:**
```json
{
  "message": "Request timestamp is in the future",
  "error_id": "7d85b5e7-d0f0-4696-b7b5-a300d0d03a5e",
  "timestamp": 3318215482991
}
```

---

### 5XX – Server Error

**Example Response Body:**
```json
{
  "message": "Something went wrong!",
  "error_id": "7d85b5e7-d0f0-4696-b7b5-a300d0d03a5e",
  "timestamp": 3318215482991
}
```
