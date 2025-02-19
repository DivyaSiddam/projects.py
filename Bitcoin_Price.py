import sys
import requests

class BitcoinPriceFetcher:
    def __init__(self):
        self.api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    def get_price_in_usd(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            
            data = response.json()
            price_in_usd = data['bitcoin']['usd']
           

            return f"{price_in_usd:.2f}"

        except requests.exceptions.RequestException as e:
            print("Error fetching Bitcoin price:", e)
            sys.exit(1)  # Exit on failure

# Create an instance of the class
btc_fetcher = BitcoinPriceFetcher()

# Print the formatted Bitcoin price
print(f"The current bitcoin price in USD is ${btc_fetcher.get_price_in_usd()}")
