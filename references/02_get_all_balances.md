# Get All Balances

> `GET /balances`

Get crypto exchange account balances for the requesting user. The user is resolved by the provided API key.

> **Note:** Rate limit: 1000 requests per minute.

---

## Request

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
curl -L -X GET 'https://revx.revolut.com/api/1.0/balances' \
  -H 'Accept: application/json' \
  -H 'X-Revx-API-Key: <API_KEY_VALUE>'
```

---

## Response

### 200 – OK

The list of available balances.

**Body:** `array of objects`

Each object in the array contains:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `currency` | string | ✅ Required | Currency symbol. Example: `"BTC"`. |
| `available` | string | ✅ Required | Available (free) funds amount. Returned as a string to prevent rounding errors. Example: `"1000.0000"`. |
| `reserved` | string | ✅ Required | Reserved (locked) funds amount. Returned as a string to prevent rounding errors. Example: `"234.5000"`. |
| `total` | string | ✅ Required | Available + Reserved funds amount. Returned as a string to prevent rounding errors. Example: `"1234.5000"`. |

**Example Response Body:**
```json
[
  {
    "currency": "BTC",
    "available": "1000.00000000",
    "reserved": "234.50000000",
    "total": "1234.50000000"
  },
  {
    "currency": "ETH",
    "available": "1000.0000",
    "reserved": "234.5000",
    "total": "1234.5000"
  }
]
```

---

### 401 – Unauthorized

**Body:** `object`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `error_id` | string (uuid) | ✅ Required | Unique identifier for this specific error occurrence. |
| `message` | string | ✅ Required | Human-readable description of the error. |
| `timestamp` | integer (int64) | ✅ Required | The time the error occurred in Unix epoch milliseconds. |

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
