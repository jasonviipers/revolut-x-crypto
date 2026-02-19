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
3. **Request Path** — the full path including query parameters (e.g., `/api/1.0/balances`)
4. **Request Body** — the hashed JSON body string (if present)

#### Construct the Message String

```
{TIMESTAMP}{HTTP_METHOD}{REQUEST_PATH}{REQUEST_BODY}
```

**Example Message:**
```
1746007718237GET/api/1.0/balances
```

---

### Sign the Message

Sign the constructed message string using your Ed25519 private key.

1. Base64-encode the resulting signature.
2. Send this value in the `X-Revx-Signature` header.

---

### Code Examples

#### Python

```python
import base64
import time
from pathlib import Path
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

# 1. Load the private key
private_key_pem = Path("private_key.pem").read_bytes()
private_key = serialization.load_pem_private_key(private_key_pem, password=None)

# 2. Prepare the message
timestamp = str(int(time.time() * 1000))
method = "GET"
path = "/api/1.0/configuration/currencies"
body = ""
message = f"{timestamp}{method}{path}{body}"

# 3. Sign the message
signature = private_key.sign(message.encode("utf-8"))
encoded_signature = base64.b64encode(signature).decode("utf-8")

# 4. Use the signature in the X-Revx-Signature header
print(f"X-Revx-Signature: {encoded_signature}")
```

#### Node.js

```javascript
const crypto = require("crypto");
const fs = require("fs");

// 1. Load the private key
const privateKey = fs.readFileSync("private_key.pem", "utf8");

// 2. Prepare the message
const timestamp = Date.now().toString();
const method = "GET";
const path = "/api/1.0/configuration/currencies";
const body = "";
const message = `${timestamp}${method}${path}${body}`;

// 3. Sign the message
const sign = crypto.createSign("ed25519");
sign.update(message);
const signature = sign.sign(privateKey, "base64");

// 4. Use the signature in the X-Revx-Signature header
console.log(`X-Revx-Signature: ${signature}`);
```

---

## API Endpoints

To use the references for specific endpoints and operations of this API, browse the docs on the left.

### Base URL

```
https://revx.revolut.com/api/1.0
```

### Authentication

**Security Scheme Type:** `apiKey`

**Header parameter name:** `X-Revx-API-Key`
