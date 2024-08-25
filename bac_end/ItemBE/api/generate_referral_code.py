# from .models import Item

# def generate_referral_code(item):
       
#         item_code = item.ItemCode
        
#         item_name_chars = item.ItemName[:4]
        
#         item_sku_chars = item.SKU[:4]

#         if len(item_name_chars) < 4:
#            remaining_chars = 4 - len(item_name_chars)
#            item_name_chars += item_code[:remaining_chars]
        
#         item.ReferralCode = f"RF{item_name_chars}{item_sku_chars}"

#         existing_referral_codes = Item.objects.filter(ReferralCode=item.ReferralCode)
        
        
#         if existing_referral_codes.exists():
#         # If the generated code exists, modify it to make it unique
#            suffix = 1
#            while True:
#               modified_referral_code = f"{item.ReferralCode}{suffix}"
#               if not Item.objects.filter(ReferralCode=modified_referral_code).exists():
#                   generated_referral_code = modified_referral_code
#                   break
#                   suffix += 1


        
#         item.save()

# Referral Code Generation Algorithm
from .models import Item
import random
import string  # Import the requests library
import requests
def is_referral_code_unique(referral_code):
    # Define your API endpoint URL
    api_url = "http://127.0.0.1:8000/api/all/"
    payload = {"ReferralCode": referral_code}
    
    try:
        response = requests.get(api_url, params=payload)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        result = response.json()
        return result.get("unique", False)
    except requests.exceptions.RequestException as e:
        # Handle API request errors here
        print(f"API request error: {e}")
        return False

def generate_referral_code(item):
    item_code = item.ItemCode
    item_name_chars = item.ItemName[:4]
    item_sku_chars = int(item.SKU[:4])
    
    if len(item_name_chars) < 4:
        remaining_chars = 4 - len(item_name_chars)
        item_name_chars += item_code[:remaining_chars]
    
    base_referral_code = f"RF{item_name_chars}{item_sku_chars}"
    
    # Check if the referral code is unique using the API
    if is_referral_code_unique(base_referral_code):
        item.ReferralCode = base_referral_code
    else:
        # Generate a random 2-character alphanumeric string
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=2))

        item.ReferralCode = f"{base_referral_code[:8]}{random_chars}"
    
    item.save()
