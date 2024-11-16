import requests
from bs4 import BeautifulSoup

# List of product URLs to check
urls = [
    'https://caresmith.com/products/revive-electric-head-massager',  # Replace with your product URLs
    'https://caresmith.com/products/x-massage-gun',
    'https://caresmith.com/products/revive-electric-head-massager?variant=44546776301731'
]

# Function to check product availability
def check_availability():
    out_of_stock_items = []

    for url in urls:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the button with the class 'product-form__submit' and check if it is disabled
            button = soup.find('button', class_='product-form__submit')

            # Check if button is found and has 'Sold out' text
            if button and 'Sold out' in button.get_text() and button.has_attr('disabled'):
                out_of_stock_items.append(url)
        else:
            print(f"Failed to fetch the page for {url}")

    if out_of_stock_items:
        print("The following products are out of stock:")
        for item in out_of_stock_items:
            print(item)
    else:
        print("All products are in stock.")

# Run the availability check function one time
if __name__ == "__main__":
    check_availability()
