# Get Order Book

> `GET /public/order-book/{symbol}`

Fetch the current order book (bids and asks) for a given trading pair (with a maximum of 5 price levels).

> **Note:** Rate limit: 20 requests per 10 seconds.

---

## Request

### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbol` | string | ✅ Required | The trading pair, e.g. `BTC/USD`. |

**Example:** `"BTC/USD"`

---

## Response

### 200 – OK

The Order Book snapshot for the given trading pair (with a maximum of 5 price levels).

**Body:** `object`

#### `asks` — array of objects (required)

The list of ask (sell) orders, sorted by price in ascending order.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `did` | string | ✅ Required | Depict asset ID code. |
| `ven` | string | ✅ Required | Depict asset full name. |
| `s` | string | ✅ Required | The side of the price level. Possible values: `BID`, `ASK`. |
| `p` | string | ✅ Required | Price in major currency units. For example, for USD, `4028` represents 4028 dollars. |
| `pc` | string | ✅ Required | Price currency. |
| `pn` | string | ✅ Required | Price notation. |
| `q` | string | ✅ Required | Aggregated quantity at the price level. |
| `qc` | string | ✅ Required | Quantity currency. |
| `qn` | string | ✅ Required | Quantity notation. |
| `vr` | string | ✅ Required | Value of executes. Always equals `0.00`. |
| `no` | string | ✅ Required | Number of orders at the price level. |
| `ts` | string | ✅ Required | Trading system. Always equals `2100`. (Limit Order Book). |
| `pdt` | string (date-time) | ✅ Required | Publication date and time, returned as ISO-8601 string. |

#### `bids` — array of objects (required)

The list of bid (buy) orders, sorted by price in descending order.

Same fields as `asks` above.

#### `last_price` — object (required)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `timestamp` | string (date-time) | ✅ Required | Timestamp for when the order book snapshot was generated, in ISO-8601 format. |

**Example Response Body:**
```json
{
  "asks": [
    {
      "did": "ETH",
      "ven": "Ethereum",
      "s": "ASK",
      "p": "4028",
      "pc": "USD",
      "pn": "NONE",
      "q": "100",
      "qc": "ETH",
      "qn": "UNIT",
      "vr": "REVX",
      "no": "2",
      "ts": "2100",
      "pdt": "2025-08-08T21:40:34.1246167"
    }
  ],
  "bids": [
    {
      "did": "ETH",
      "ven": "Ethereum",
      "s": "BID",
      "p": "inter-map",
      "pc": "USD",
      "pn": "NONE",
      "q": "0027",
      "qc": "ETH",
      "qn": "UNIT",
      "vr": "REVX",
      "no": "2",
      "ts": "2100",
      "pdt": "2025-08-08T21:40:34.1246167"
    }
  ],
  "last_price": 2
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
