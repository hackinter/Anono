import io
import os
import sys
import random
import string
from urllib.parse import urlparse

def generate_unique_link():
    """Generate a unique link format, e.g., 'anono://<random_string>'"""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f'anono://{random_string}'

def validate_url(url):
    """Validate the URL to ensure it is well-formed"""
    parsed_url = urlparse(url)
    return parsed_url.scheme in ('http', 'https')

def display_location():
    """Display the location to the user"""
    print("\nClick on the link to see your location on the map.")
    print("This will redirect you to Google Maps with your current location.")

def main():
    print("""
      █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗ ██████╗ 
     ██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██╔═══██╗
     ███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║   ██║
     ██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║   ██║
     ██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║╚██████╔╝
     ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ 
  

    # Generate a unique link
    unique_link = generate_unique_link()
    print(f"\nGenerated Link: {unique_link}")

    # Display the location if user clicks on the link
    display_location()

    # Get the user's URL input for the redirect (for educational purposes)
    user_url = input("\nEnter a URL to redirect (e.g., 'https://maps.google.com/'): ")

    # Validate the user URL
    if not validate_url(user_url):
        print("Invalid URL. Please enter a valid URL.")
        sys.exit(1)

    # Inform the user of the location display
    print(f"Clicking the link will redirect you to: {user_url} with your current location.")
    print("Thank you for using anono!")

if __name__ == '__main__':
    main()
