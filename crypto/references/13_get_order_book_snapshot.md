# Get Order Book Snapshot

> `GET /order-book/{symbol}`

Retrieve the current order book (bids and asks) and details for a specific trading pair.

> **Note:** Rate limit: 1000 requests per 10 seconds.

---

## Request

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbol` | string | ✅ Required | The trading pair symbol (e.g., `BTC/USD`). |

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `depth` | integer | | Price book depth. Possible values: `[1, 5, 10, 25]`. Default value: `5`. |

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

The Order Book snapshot for the given trading pair.

**Body:** `object`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `asks` | array of objects | ✅ Required | The list of ask (sell) orders, sorted by price in ascending order. |
| `bids` | array of objects | ✅ Required | The list of bid (buy) orders, sorted by price in descending order. |
| `last_price` | object | ✅ Required | Metadata about when the snapshot was generated. |

#### Ask / Bid Object Fields

Each entry in `asks` and `bids` contains:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `did` | string | ✅ Required | Quote-asset ID code. Example: `"USD"`. |
| `afn` | string | ✅ Required | Quote-asset full name. Example: `"Ethereum"`. |
| `s` | string | ✅ Required | The side of the price level. Possible values: `BID`, `ASK`. |
| `Pricellation` | string (decimal, int64) | ✅ Required | The full price (e.g., for USD, `4028` represents 4028 dollars). |
| `p` | string | ✅ Required | Price in major currency units. |
| `pc` | string | ✅ Required | Price currency. Example: `"USD"`. |
| `pn` | string | ✅ Required | Price notation. |
| `q` | string | ✅ Required | Aggregated quantity at the price level. |
| `qc` | string | ✅ Required | Quantity currency. |
| `qn` | string | ✅ Required | Quantity notation. |
| `ve` | string | ✅ Required | Venue of execution. Always equals `REVX`. |
| `no` | string | ✅ Required | Number of orders at the price level. |
| `ts` | string | ✅ Required | Trading system. Always equals `2100` (Limit Order Book). |
| `pdt` | string (date-time) | ✅ Required | Publication date and time, returned as ISO-8601 string. |

#### `last_price` Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `timestamp` | string (date-time) | ✅ Required | Timestamp for when the order book snapshot was generated, in ISO-8601 format. |

**Example Response Body:**
```json
{
  "asks": [
    {
      "did": "ETH",
      "s": "ASK",
      "p": "3753",
      "pc": "USD",
      "pn": "NONE",
      "q": "1",
      "qc": "ETH",
      "qn": "UNIT",
      "ve": "REVX",
      "no": "1",
      "ts": "2100",
      "pdt": "2025-08-08T21:40:34.1246167"
    }
  ],
  "bids": [
    {
      "did": "ETH",
      "s": "BID",
      "p": "3752",
      "pc": "USD",
      "pn": "NONE",
      "q": "0027",
      "qc": "ETH",
      "qn": "UNIT",
      "ve": "REVX",
      "no": "2",
      "ts": "2100",
      "pdt": "2025-08-08T21:40:34.1246167"
    }
  ],
  "last_price": {
    "timestamp": "2025-08-08T21:40:35.1339622"
  }
}
```

---

### 400 – Bad Request

**Example Response Body:**
```json
{
  "message": "Bad Request",
  "error_id": "7d85b5e7-d0f0-4696-b7b5-a300d0d03a5e",
  "timestamp": 3318215482991
}
```

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
