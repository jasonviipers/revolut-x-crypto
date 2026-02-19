# Get Historical OHLCV Candles

> `GET /candles/{symbol}`

Retrieve historical market data (Open, High, Low, Close, Volume) for a specific symbol. If there is trading volume, the view is based on recent trades. If there is no volume, the view is based on the Mid Price (Bid/Ask average).

> **Note:** Rate limit: 1000 requests per minute.

---

## Request

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbol` | string | ✅ Required | The trading pair symbol (e.g., `BTC-USD`). |

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `interval` | integer (int32) | | Time interval between candles in minutes. Possible values: `[5, 15, 30, 60, 240, 1440, 2880, 5760, 10000, 20160, 40320]`. Example: `5`. Default value: `5`. |
| `since` | integer (int64) | | Start timestamp for the query in Unix epoch milliseconds. Example: `3318215482991`. Logic: if not provided, returns the last 100 candles based on the interval. If provided but the range is too large, results will be truncated to the last 100 candles before the current timestamp. |

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

### Example cURL

```bash
curl -L -g -X GET 'https://revx.revolut.com/api/1.0/candles/{symbol}' \
  -H 'Accept: application/json' \
  -H 'X-Revx-API-Key: <API_KEY_VALUE>'
```

---

## Response

### 200 – OK

List of OHLCV candles.

**Body:** `object`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | array of objects | ✅ Required | List of candle records. |

Each candle object in `data` contains:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `start` | integer (int64) | ✅ Required | Start timestamp of the candle in Unix epoch milliseconds. |
| `open` | string (decimal) | ✅ Required | Opening price during the interval. |
| `high` | string (decimal) | ✅ Required | Highest price during the interval. |
| `low` | string (decimal) | ✅ Required | Lowest price during the interval. |
| `close` | string (decimal) | ✅ Required | Closing price. |
| `volume` | string (decimal) | ✅ Required | Total trading volume during the interval. |

**Example Response Body:**
```json
{
  "data": [
    {
      "start": 3318215482991,
      "open": "92087.81",
      "high": "92133.89",
      "low": "92052.39",
      "close": "92067.31",
      "volume": "0.00067964"
    },
    {
      "start": 3318215782991,
      "open": "90390.46",
      "high": "90395",
      "low": "90358.84",
      "close": "90395",
      "volume": "0.00230816"
    }
  ]
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
