# Get Last Trades

> `GET /public/last-trades`

Get the list of the latest 100 trades executed on Revolut X crypto exchange.

> **Note:** Rate limit: 20 requests per 10 seconds.

---

## Request

No authentication or parameters are required for this endpoint.

### Example cURL

```bash
curl -L -X GET 'https://revx.revolut.com/api/1.0/public/last-trades' \
  -H 'Accept: application/json'
```

---

## Response

### 200 – OK

The list of the latest trades executed on Revolut X crypto exchange.

**Body:** `object`

#### `data` — array of objects (required)

The list of the latest trade records.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `tdt` | string (date-time) | ✅ Required | Trading date and time, returned as ISO-8601 string. Example: `"2025-08-08T21:40:35.1339622"`. |
| `aid` | string | ✅ Required | Crypto-asset ID code. Example: `"BTC"`. |
| `anm` | string | ✅ Required | Crypto-asset full name. Example: `"Bitcoin"`. |
| `p` | string | ✅ Required | Price in major currency units. For example, for USD, `116243.32` represents 116243.32 dollars. Example: `"116243.32"`. |
| `pc` | string | ✅ Required | Price currency. Example: `"USD"`. |
| `pn` | string | ✅ Required | Price notation. Example: `"NONE"`. |
| `q` | string | ✅ Required | Quantity. Example: `"0.24521000"`. |
| `qc` | string | ✅ Required | Quantity currency. Example: `"BTC"`. |
| `qn` | string | ✅ Required | Quantity notation. Example: `"UNIT"`. |
| `ve` | string | ✅ Required | Venue of execution. Always equals `REVX`. |
| `pdt` | string (date-time) | ✅ Required | Publication date and time, returned as ISO-8601 string. |
| `vp` | string | ✅ Required | Venue of publication. Always equals `REVX`. |
| `tid` | string | ✅ Required | Transaction identification code. Example: `"5ef9648f658149f7ababedc97a6401f8"`. |

#### `metadata` — object (required)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `timestamp` | string (date-time) | ✅ Required | Timestamp when the data was generated, returned as ISO-8601 string. |

**Example Response Body:**
```json
{
  "data": [
    {
      "tdt": "2025-08-08T21:40:35.1339622",
      "aid": "BTC",
      "anm": "Bitcoin",
      "p": "116243.32",
      "pc": "USD",
      "pn": "NONE",
      "q": "0.24521000",
      "qc": "BTC",
      "qn": "UNIT",
      "ve": "REVX",
      "pdt": "2025-08-08T21:40:35.1339622",
      "vp": "REVX",
      "tid": "5ef9648f658149f7ababedc97a6401f8"
    },
    {
      "tdt": "2025-08-08T21:40:34.1324652",
      "aid": "ETH",
      "anm": "Ethereum",
      "p": "4028.23",
      "pc": "USDC",
      "pn": "NONE",
      "q": "12.00000000",
      "qc": "ETH",
      "qn": "UNIT",
      "ve": "REVX",
      "pdt": "2025-08-08T21:40:34.1324652",
      "vp": "REVX",
      "tid": "3b2b202b766843cfa6c8b3354e7f4c52"
    }
  ],
  "metadata": {
    "timestamp": "2025-08-08T21:40:36.684333Z"
  }
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
