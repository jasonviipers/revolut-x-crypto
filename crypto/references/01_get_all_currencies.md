# Get All Currencies

> `GET /configuration/currencies`

Get configuration for all currencies used on the exchange.

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
curl -L -X GET 'https://revx.revolut.com/api/1.0/configuration/currencies' \
  -H 'Accept: application/json' \
  -H 'X-Revx-API-Key: <API_KEY_VALUE>'
```

---

## Response

### 200 – OK

Supported currencies with their details.

**Body:** `object`

Each key is a currency symbol mapping to an object with the following fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `symbol` | string | ✅ Required | The symbol of the currency. |
| `name` | string | ✅ Required | The full name of the currency. |
| `scale` | integer | ✅ Required | The number of decimal places used to express the currency's smallest unit. For example, a scale of `8` means precision up to `0.00000001`. |
| `asset_type` | string | ✅ Required | The type of the currency. Possible values: `fiat`, `crypto`. |
| `status` | string | ✅ Required | The status of the currency. Possible values: `active`, `inactive`. |

**Example Response Body:**
```json
{
  "BTC": {
    "symbol": "BTC",
    "name": "Bitcoin",
    "scale": 8,
    "asset_type": "crypto",
    "status": "active"
  },
  "ETH": {
    "symbol": "ETH",
    "name": "Ethereum",
    "scale": 8,
    "asset_type": "crypto",
    "status": "active"
  }
}
```

---

### 401 – Unauthorized

**Body:** `object`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `error_id` | string (uuid) | ✅ Required | Unique identifier for this specific error occurrence. |
| `message` | string | ✅ Required | Human-readable description of the error. |
| `timestamp` | integer (int64) | ✅ Required | The time the error occurred in Unix epoch milliseconds. |

**Example Response Body:**
```json
{
  "message": "API key can only be used for authentication f...",
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
