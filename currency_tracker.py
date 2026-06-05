import urllib.request
import json

def get_live_rates():
    """Fetches real-time currency exchange rates from a reliable public API."""
    url = "https://open.er-api.com/v6/latest/USD"
    try:
        # Sending request to the live currency API
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            if data["result"] == "success":
                return data["rates"]
            else:
                return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    """Converts the given amount from one currency to another using live rates."""
    if from_currency not in rates or to_currency not in rates:
        return None
    
    # First, convert the amount to USD base, then to the target currency
    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]
    return round(converted_amount, 2)

# --- Main Program Execution ---
print("=== Real-Time Smart Currency Converter ===")
print("Fetching latest live market rates... Please wait.\n")

live_rates = get_live_rates()

if live_rates:
    print("✅ Live rates successfully loaded from Global Finance Market!")
    print("-----------------------------------------------------")
    
    # Supported common currencies for quick reference
    print("Supported Currency Codes: BDT, USD, EUR, INR, GBP, CAD, AED")
    print("-----------------------------------------------------")
    
    try:
        # Taking inputs from user
        amount = float(input("Enter the amount to convert: "))
        from_curr = input("From Currency (e.g., USD): ").upper().strip()
        to_curr = input("To Currency (e.g., BDT): ").upper().strip()
        
        # Performing calculations
        result = convert_currency(amount, from_curr, to_curr, live_rates)
        
        if result is not None:
            print(f"\n📊 CONVERSION RESULT:")
            print(f"👉 {amount:,} {from_curr} = {result:,} {to_curr}")
        else:
            print("\n❌ Error: Invalid currency code entered. Please try again.")
            
    except ValueError:
        print("\n❌ Error: Please enter a valid number for the amount.")
else:
    print("\n❌ Failed to connect to the live rate network. Check your internet connection!")

print("\n=====================================================")
