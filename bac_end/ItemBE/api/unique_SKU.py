from .models import Item
import random
import string  # Import the requests library
import requests
def is_sku_unique(sku):
    api_url = "http://127.0.0.1:8000/api/all/"
    print(sku)
    payload = {"SKU": sku}
    
    
    try:
        response = requests.get(api_url, params=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("unique", False)
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return False