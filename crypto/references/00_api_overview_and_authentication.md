# Revolut X Crypto Exchange REST API

## Overview

As a Revolut X customer, you can use the Revolut X REST API to interact with the exchange, create & follow your orders, and more.

---

## API Key

To get started using the Revolut X API, an API key is used to authenticate your requests, to create & follow your orders, and for other exchange interactions.

Before configuring your API key on the Revolut X platform, you must first set it up locally. You can generate the key set using the following commands.

---

### 1. Generate the Private Key

Run the following command in your terminal:

```bash
openssl genpkey -algorithm ed25519 -out private_key.pem
```

This command produces a file named `private_key.pem` which contains your private key. It has the following structure:

```
-----BEGIN PRIVATE KEY-----
<base64-encoded private key data>
-----END PRIVATE KEY-----
```

> **⚠️ DANGER: Secure your private key.**
> This is your **private** key. Do not share it with anyone. **Your private key is a secret.** Store it securely in a safe place and never expose it in public repositories or share it with other people.

---

### 2. Generate the Public Key

Extract the public key from your private key:

```bash
openssl pkey -in private_key.pem -pubout -out public_key.pem
```

The generated public key will be saved in a file named `public_key.pem`. It has the following structure:

```
-----BEGIN PUBLIC KEY-----
YOUR PUBLIC ED25519 PUBLIC KEY
-----END PUBLIC KEY-----
```

---

### 3. Upload Your Public Key

This is your public key. You can freely share it. Upload it to the Revolut X platform by going to **Settings → Profile** in the developer portal.

---

### Create Your API Key

Once you have your public key file, link it on the exchange platform by navigating to the **Developer Settings → Profile** to create your API key.

---

## Authentication Headers

The Revolut X REST API uses a header-based authentication scheme. Every API request must include the following headers:

| Header | Description |
|--------|-------------|
| `X-Revx-API-Key` | An API Key string used to identify the API key used. |
| `X-Revx-Timestamp` | The Unix time in milliseconds at the time of the request. |
| `X-Revx-Signature` | The request digest signed with your **private key**. |

---

## Signing a Request

The signature process ensures authenticity. The signature is constructed from the following components in order:

1. **Timestamp** — Unix time in milliseconds (the `X-Revx-Timestamp` header value)
2. **HTTP Method** — uppercase string, e.g. `GET`, `POST`
3. **Request Path** — the full path including query parameters (e.g., `/api/1.0/orders/active`)
4. **Query String** — The URL query string if present (e.g.,`limit=10`). Do not include the `?.`
5. **Request Body** — The minified JSON body string, if present.

> **Note**
> When concatenating, do not add any separators (spaces, newlines, or commas) between the fields.

**Example Message:**

```json
1765360896219POST/api/1.0/orders{"client_order_id":"3b364427-1f4f-4f66-9935-86b6fb115d26","symbol":"BTC-USD","side":"BUY","order_configuration":{"limit":{"base_size":"0.1","price":"90000.1"}}}
```

## 2. Sign the message

1. Sign the constructed string using your **Ed25519 private key**.
2. **Base64-encode** the resulting signature.
3. Send this value in the `X-Revx-Signature` header.

### Code Examples

#### Python
```python
    import base64
    from pathlib import Path
    from nacl.signing import SigningKey
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.backends import default_backend

    # 1. Load your Private Key
    pem_data = Path("private.pem").read_bytes()
    private_key_obj = serialization.load_pem_private_key(
        pem_data,
        password=None,
        backend=default_backend()
    )

    # Extract raw bytes for PyNaCl
    raw_private = private_key_obj.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )

    # 2. Prepare the message
    timestamp = "1746007718237"
    method = "GET"
    path = "/api/1.0/orders/active"
    query = "status=open&limit=10"
    body = "" # Empty for GET

    # Concatenate without separators
    message = f"{timestamp}{method}{path}{query}{body}".encode('utf-8')

    # 3. Sign and Encode
    signing_key = SigningKey(raw_private)
    signed = signing_key.sign(message)
    signature = base64.b64encode(signed.signature).decode()

    print(f"X-Revx-Signature: {signature}")
```

#### Node.js

```javascript
    const crypto = require('crypto');
    const fs = require('fs');

    // 1. Load your Private Key
    const privateKey = fs.readFileSync('private.pem', 'utf8');

    // 2. Prepare the message
    const timestamp = Date.now().toString();
    const method = 'POST';
    const path = '/api/1.0/crypto-exchange/orders';
    const body = JSON.stringify({
    symbol: "BTC/USD",
    type: "limit",
    side: "buy",
    qty: "0.005"
    });

    // Concatenate without separators
    const message = timestamp + method + path + body;

    // 3. Sign and Encode
    // Note: Use crypto.sign with null to indicate pure Ed25519 signing (no hashing algorithm)
    const signatureBuffer = crypto.sign(null, Buffer.from(message), privateKey);
    const signature = signatureBuffer.toString('base64');

    console.log(`X-Revx-Timestamp: ${timestamp}`);
    console.log(`X-Revx-Signature: ${signature}`);
```

## API Endpoints

To use the references for specific endpoints and operations of this API, browse the docs on the left.

### Base URL

```
https://revx.revolut.com/api/1.0
```

### Authentication

**Security Scheme Type:** `apiKey`

**Header parameter name:** `X-Revx-API-Key`
