 # Revolut X Crypto API Client and References
 
 A minimal, practical toolkit for interacting with the Revolut X Crypto Exchange REST API. It includes:
 - A Python client for authenticated requests and trading
 - Reference docs for common endpoints and workflows
 
 ## Features
 - Ed25519-based request signing and header auth
 - Fetch market data: currencies, pairs, order book, trades, OHLCV
 - Manage orders: place, cancel, query by ID
 - Retrieve account balances
 
 ## Prerequisites
 - Python 3.10+ recommended
 - OpenSSL (for generating Ed25519 keys)
 - Python packages: `requests`, `cryptography`
 
 ## Installation
 Install required packages:
 
 ```bash
 pip install requests cryptography
 ```
 
 ## Generate Keys and Get API Access
 1) Generate a private key:
 
 ```bash
 openssl genpkey -algorithm ed25519 -out private_key.pem
 ```
 
 2) Derive the public key:
 
 ```bash
 openssl pkey -in private_key.pem -pubout -out public_key.pem
 ```
 
 3) Upload the public key and create an API key in the Revolut X developer portal (Settings → Profile).
 
 See detailed steps in [00_api_overview_and_authentication.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/00_api_overview_and_authentication.md).
 
 ## Quick Start (Python)
 Use the Python client to sign requests and call endpoints.
 
 ```python
 from scripts.revolut_client import RevolutClient
 
 client = RevolutClient(
     private_key_path="path/to/private_key.pem",
     api_key="your_api_key"
 )
 
 # Market/configuration data
 currencies = client.get_currencies()
 print(currencies)
 
 # Account balances
 balances = client.get_balances()
 print(balances)
 
 # Place a limit order (example)
 order = client.place_order(
     client_order_id="unique_id_123",
     symbol="BTC-USD",
     side="buy",
     order_configuration={
         "limit": {
             "price": "50000",
             "base_size": "0.001"
         }
     }
 )
 print(order)
 ```
 
 Client source: [revolut_client.py](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/scripts/revolut_client.py)
 
 ## API Reference
 Explore endpoint guides in the `references/` folder:
 - [01_get_all_currencies.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/01_get_all_currencies.md)
 - [02_get_all_balances.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/02_get_all_balances.md)
 - [03_get_all_currency_pairs.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/03_get_all_currency_pairs.md)
 - [04_get_order_book.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/04_get_order_book.md)
 - [05_get_last_trades.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/05_get_last_trades.md)
 - [06_place_order.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/06_place_order.md)
 - [07_get_active_orders.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/07_get_active_orders.md)
 - [08_get_historical_orders.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/08_get_historical_orders.md)
 - [09_get_order_by_id.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/09_get_order_by_id.md)
 - [10_cancel_order_by_id.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/10_cancel_order_by_id.md)
 - [11_get_fills_of_order_by_id.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/11_get_fills_of_order_by_id.md)
 - [12_get_client_trades.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/12_get_client_trades.md)
 - [14_get_historical_ohlcv_candles.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/14_get_historical_ohlcv_candles.md)
 - [15_get_all_tickers.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/15_get_all_tickers.md)
 - [16_get_all_public_trades.md](file:///c:/Users/4hkee/Downloads/revolut_api_trading/revolut-x-crypto/references/16_get_all_public_trades.md)
 
 ## Repository Structure
 - `scripts/` — Python client for authenticated API calls
 - `references/` — Task-oriented docs for common endpoints
 - `SKILL.md` — Skill overview and quick examples
 
 ## Notes and Best Practices
 - Keep `private_key.pem` outside version control; never commit secrets
 - Handle HTTP errors and rate limits; inspect status codes and response text
 - Properly encode query parameters when signing; see client notes around signing
 
 ## Disclaimer
 This repository is for educational and integration guidance. Validate against the latest Revolut X API documentation and test in a safe environment before live trading.
