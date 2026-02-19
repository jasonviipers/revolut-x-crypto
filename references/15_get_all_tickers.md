# Get All Tickers

> `GET /tickers`

Retrieves the latest market data snapshots for all supported currency pairs. The response includes the current best bid and ask prices, the calculated mid-price, and the last traded price for each active symbol.

> **Note:** Rate limit: 1000 requests per minute.

---

## Request

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbols` | array of strings | | Filter tickers by specific currency pairs (comma-separated). |

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
curl -L -X GET 'https://revx.revolut.com/api/1.0/tickers' \
  -H 'Accept: application/json' \
  -H 'X-Revx-API-Key: <API_KEY_VALUE>'
```

---

## Response

### 200 – OK

The list of tickers.

**Body:** `object`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `data` | array of objects | ✅ Required | List of ticker information for currency pairs. |
| `metadata` | object | ✅ Required | Metadata about the response. |

Each ticker object in `data` contains:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `symbol` | string | ✅ Required | The unique identifier for the currency pair (e.g., `BTC/USD`). Example: `"BTC/USD"`. |
| `bid` | string (decimal) | ✅ Required | The current highest price a buyer is willing to pay. Represents the top price in the buy order book. Example: `"65100.50"`. |
| `ask` | string (decimal) | ✅ Required | The current lowest price a seller is willing to accept. Represents the top price in the sell order book. Example: `"65101.00"`. |
| `mid` | string (decimal) | ✅ Required | The arithmetic midpoint between the best bid and best ask prices. Calculated as `(bid + ask) / 2`. |
| `last_price` | string (decimal) | ✅ Required | The price at which the most recent trade was successfully executed. Example: `"65101.00"`. |

The `metadata` object contains:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `timestamp` | integer (int64) | ✅ Required | The time the data was captured in Unix epoch milliseconds. Example: `1770201294631`. |

**Example Response Body:**
```json
{
  "data": [
    {
      "symbol": "BTC/USD",
      "bid": "0.02",
      "ask": "0.02",
      "mid": "0.02",
      "last_price": "0.02"
    },
    {
      "symbol": "ETH/USD",
      "bid": "0.02",
      "ask": "0.03",
      "mid": "0.02",
      "last_price": "0.02"
    }
  ],
  "metadata": {
    "timestamp": 1770201294631
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

### 5XX – Server Error

**Example Response Body:**
```json
{
  "message": "Something went wrong!",
  "error_id": "7d85b5e7-d0f0-4696-b7b5-a300d0d03a5e",
  "timestamp": 3318215482991
}
```
