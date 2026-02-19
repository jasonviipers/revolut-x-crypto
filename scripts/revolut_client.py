import base64
import time
import json
import requests
from pathlib import Path
from typing import Optional, Dict, Any, List
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

class RevolutClient:
    """
    A client for the Revolut X Crypto Exchange REST API.
    Handles authentication and request signing.
    """

    BASE_URL = "https://revx.revolut.com/api/1.0"

    def __init__(self, private_key_path: str, api_key: str):
        """
        Initialize the client.

        Args:
            private_key_path: Path to the private key file (PEM format).
            api_key: The API key string (X-Revx-API-Key).
        """
        self.api_key = api_key
        self.private_key = self._load_private_key(private_key_path)

    def _load_private_key(self, path: str) -> Ed25519PrivateKey:
        """Load the Ed25519 private key from a PEM file."""
        try:
            private_key_pem = Path(path).read_bytes()
            return serialization.load_pem_private_key(private_key_pem, password=None)
        except Exception as e:
            raise ValueError(f"Failed to load private key from {path}: {e}")

    def _sign_request(self, method: str, path: str, body: str = "") -> Dict[str, str]:
        """
        Generate the authentication headers for a request.
        
        Args:
            method: HTTP method (GET, POST, etc.).
            path: Request path (e.g., /api/1.0/balances).
            body: Request body string (empty for GET).
            
        Returns:
            A dictionary containing the required headers.
        """
        timestamp = str(int(time.time() * 1000))
        message = f"{timestamp}{method}{path}{body}"
        
        signature = self.private_key.sign(message.encode("utf-8"))
        encoded_signature = base64.b64encode(signature).decode("utf-8")
        
        return {
            "X-Revx-API-Key": self.api_key,
            "X-Revx-Timestamp": timestamp,
            "X-Revx-Signature": encoded_signature,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def _request(self, method: str, endpoint: str, params: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict:
        """
        Make a request to the API.
        
        Args:
            method: HTTP method.
            endpoint: API endpoint (e.g., /configuration/currencies).
            params: Query parameters.
            data: JSON body data.
            
        Returns:
            The JSON response.
        """
        path = f"/api/1.0{endpoint}"
        if params:
            # Note: Query parameters should be part of the path for signing if they exist.
            # This implementation assumes simple appending for demonstration.
            # A robust implementation would properly encode params.
            from urllib.parse import urlencode
            path += "?" + urlencode(params)
            
        body_str = json.dumps(data) if data else ""
        
        headers = self._sign_request(method, path, body_str)
        url = f"{self.BASE_URL}{endpoint}"
        
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            data=body_str if data else None
        )
        
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            print(f"Response: {response.text}")
            raise

    def get_currencies(self) -> List[Dict]:
        """Get all available currencies."""
        return self._request("GET", "/configuration/currencies")

    def get_balances(self) -> List[Dict]:
        """Get all balances."""
        return self._request("GET", "/account/balances")

    def get_currency_pairs(self) -> List[Dict]:
        """Get all currency pairs."""
        return self._request("GET", "/exchange/pairs")

    def place_order(self, client_order_id: str, symbol: str, side: str, order_configuration: Dict) -> Dict:
        """
        Place a new order.
        
        Args:
            client_order_id: Unique ID for the order.
            symbol: Trading pair (e.g., BTC-USD).
            side: 'buy' or 'sell'.
            order_configuration: Dict with 'limit' or 'market' configuration.
        """
        data = {
            "client_order_id": client_order_id,
            "symbol": symbol,
            "side": side,
            "order_configuration": order_configuration
        }
        return self._request("POST", "/orders", data=data)

    def get_order(self, order_id: str) -> Dict:
        """Get an order by ID."""
        return self._request("GET", f"/orders/{order_id}")

    def cancel_order(self, order_id: str) -> Dict:
        """Cancel an order by ID."""
        return self._request("DELETE", f"/orders/{order_id}")

if __name__ == "__main__":
    # Example usage
    print("This is a library script. Import RevolutClient to use it.")
    print("Example:")
    print("client = RevolutClient('private_key.pem', 'your_api_key')")
    print("currencies = client.get_currencies()")
