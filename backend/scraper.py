"""
This script is designed to scrape MMA event data from Tapology's fight center.
It collects event details, handles pagination, and avoids duplicates using SHA-256 hashes.
"""

# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import hashlib

# Function to generate a SHA-256 hash of a string (normalized to lowercase, stripped)
def hash_string(input: str) -> str:
    """Hashes a string using SHA-256 and returns the hexadecimal digest."""
    normalized_input = input.lower().strip()
    hash_obj = hashlib.sha256(normalized_input.encode('utf-8'))
    return hash_obj.hexdigest()

# TapologyScraper class for scraping MMA event information from Tapology
class TapologyScraper:
    """
    A scraper for collecting MMA event details from Tapology's fight center.
    """

    def __init__(self, headless=True, wait_time=10):
        """
        Initializes the scraper, sets up Chrome WebDriver, and attempts to load previous data.
        
        Args:
            headless (bool): Whether to run the browser in headless mode.
            wait_time (int): Time to wait after loading a page (in seconds).
        """
        self.base_url = "https://www.tapology.com/"
        self.wait_time = wait_time
        options = webdriver.ChromeOptions()

        # Configure browser options for headless and stable operation
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--log-level=3")  # Minimize console output

        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome(options=options)

        # Try to load previously scraped data
        try:
            self.data = pd.read_csv("Events.csv")
        except FileNotFoundError:
            self.data = None

        self.scraped_data = []  # Store results during this session

    def get_event_listing_links(self, page=1):
        """
        Fetches event listing links from Tapology's fight center for a given page.
        
        Args:
            page (int): The page number to scrape (must be >= 1).
        
        Returns:
            list: URLs of individual fight events.
        """
        if page < 1:
            raise ValueError("Page number must be 1 or greater.")
        
        # Construct URL and load the page
        listing_path = f"fightcenter?group=ufc&schedule=results&sport=mma&page={page}"
        self.driver.get(self.base_url + listing_path)
        time.sleep(self.wait_time)  # Wait for page content to load

        links = []
        # Each event card is inside a div with specific data-controller attribute
        card_selectors = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-controller="bout-toggler"]')
        for card_selector in card_selectors:
            try:
                element = card_selector.find_element(By.CLASS_NAME, 'promotion').find_element(By.TAG_NAME, 'a')
                link = element.get_attribute('href')
                links.append(link)
            except Exception:
                continue  # Gracefully skip malformed cards
        return links

    def get_event_details(self, fight_url):
        """
        Scrapes the details of a single fight event.
        
        Args:
            fight_url (str): The URL of the event page.
        
        Returns:
            dict or None: Dictionary of event details or None if already scraped.
        """
        self.driver.get(fight_url)
        time.sleep(self.wait_time)

        event_details = {}

        # Locate main container with the event title
        element = self.driver.find_element(By.XPATH, '//div[contains(@class, "border-dotted") and contains(@class, "border-tap_6")]')
        title = element.find_element(By.TAG_NAME, 'h2').text
        id = hash_string(title)

        # Skip duplicate entries based on hashed ID
        if self.data is not None and id in self.data['id'].values:
            print(f"Skipping already scraped event: {title}")
            return None

        event_details['id'] = id
        event_details['title'] = title
        event_details['url'] = fight_url

        # Extract image from the primary details container
        element = self.driver.find_element(By.ID, "primaryDetailsContainer")
        img = element.find_element(By.TAG_NAME, 'img')
        event_details['image'] = img.get_attribute('src')

        return event_details

    def run(self):
        """
        Runs the scraper, navigating through pages and collecting event details.
        """
        running = True
        page = 1
        while running:
            try:
                links = self.get_event_listing_links(page=page)

                for link in links:
                    print(f"Processing event: {link}")
                    details = self.get_event_details(link)
                    if details is not None:
                        self.scraped_data.append(details)
                    else:
                        running = False  # Stop if event already scraped
                        break

                page += 1  # Move to next page
            except Exception as e:
                print(f"An error occurred: {e}")
                break  # Stop on errors (e.g., no more pages or network issues)

    def quit(self):
        """
        Saves the scraped data to CSV and shuts down the browser.
        """
        pd.DataFrame(self.scraped_data).to_csv('Events.csv', index=False)
        self.driver.quit()

# Entry point for script execution
if __name__ == "__main__":
    scraper = TapologyScraper(headless=True, wait_time=2)
    try:
        scraper.run()
    finally:
        scraper.quit()
        print("Scraper has been closed.")