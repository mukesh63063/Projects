# Selenium is used for automating web browser, like opening webpage, 
# We use for testing websites and web scraping, 
# and automating repetitive tasks in browser.

from selenium import webdriver   # automate web browser actions.
from selenium.webdriver.chrome.options import Options      # configure Chrome WebDriver settings
import time
import datetime

def display_results():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    log_file = "output/selenium_log.txt"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, "a") as f:
            f.write(f"\n[{timestamp}] Selenium started and opened http://localhost:5000\n")
    except Exception as e:
        print(f"Error writing Selenium log: {e}")

    driver.get("http://localhost:5000")
    time.sleep(5)  # Let user interact
    driver.quit()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, "a") as f:
            f.write(f"[{timestamp}] Selenium completed\n")
    except Exception as e:
        print(f"Error writing Selenium log: {e}")

if __name__ == "__main__":
    display_results()








'''

Importing Required Libraries:

The script imports selenium, time, and datetime, which are essential for web automation, delays, and timestamping logs.
Function: display_results():

Automatically opens a webpage (http://localhost:5000) using Selenium WebDriver.
Generates a log file (selenium_log.txt) to record events.
Timestamps are used to log the exact date and time of opening and closing the webpage.
Closes the webpage using driver.quit() after a 5-second delay.
This script ensures automation runs smoothly and logs each execution step with timestamps.

'''