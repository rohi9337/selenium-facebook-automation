import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import EMAIL, PASSWORD

def human_like_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(0.1 + 0.3 * random.random())  # Randomized pause between 0.1 and 0.4 seconds

def human_like_scroll(driver):
    scroll_pause_time = 0.5 + 0.5 * random.random()  # Randomized pause between 0.5 and 1.0 seconds
    for _ in range(random.randint(1, 3)):  # Random number of scrolls between 1 and 3
        driver.execute_script("window.scrollBy(0, window.innerHeight);")
        time.sleep(scroll_pause_time)

def log_message(message):
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

# Initialize Firefox WebDriver
driver = webdriver.Firefox()

# Open Facebook login page
driver.get('https://www.facebook.com/')
log_message("Navigated to Facebook login page")

try:
    # Wait for the email input field to be visible
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'email'))
    )
    log_message("Email input field located")

    # Simulate human-like typing for email/phone input
    human_like_typing(email_input, EMAIL)

    # Human-like scrolling
    human_like_scroll(driver)

    # Wait for a moment before entering password
    time.sleep(1.5 + 0.5 * random.random())  # Simulating human delay

    # Find the password input field
    password_input = driver.find_element(By.ID, 'pass')
    log_message("Password input field located")

    # Simulate human-like typing for password input
    human_like_typing(password_input, PASSWORD)

    # Human-like scrolling
    human_like_scroll(driver)

    # Wait before clicking the login button
    time.sleep(1.5 + 0.5 * random.random())  # Simulating human delay

    # Find and click the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'login'))
    )
    log_message("Login button located")
    login_button.click()
    log_message("Login button clicked")

    # Wait until the home page loads by waiting for the home icon to be visible
    home_icon = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//a[@aria-label="Home"]'))
    )
    log_message("Home page loaded")

    # List of usernames to search for
    usernames = ["mg.yo.374"]  # Add more usernames as needed

    for username in usernames:
        log_message(f"Searching for user: {username}")

        # Wait for the search input field to be visible
        search_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@aria-label="Search Facebook"]'))
        )
        log_message("Search input field located")

        # Clear any previous search using JavaScript to ensure the input field is completely cleared
        search_input.send_keys(Keys.CONTROL + "a")
        time.sleep(0.1 + 0.2 * random.random())  # Add a slight random delay before clearing
        search_input.send_keys(Keys.BACKSPACE)
        time.sleep(0.5)  # Slight delay to ensure clearing

        # Focus on the search input field using JavaScript
        driver.execute_script("arguments[0].click();", search_input)
        time.sleep(0.5)  # Slight delay to ensure focus

        # Simulate human-like typing in the search input field
        human_like_typing(search_input, username)

        # Press Enter to perform the search
        search_input.send_keys(Keys.ENTER)
        log_message("Search executed")

        # Wait for search results to load and locate the profile link
        profile_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f'//a[contains(@href, "{username}")]'))
        )
        log_message("Profile link located")

        # Ensure the profile link is clickable by scrolling it into view and using JavaScript click
        driver.execute_script("arguments[0].scrollIntoView(true);", profile_link)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'//a[@href="https://www.facebook.com/{username}"]')))
        driver.execute_script("arguments[0].click();", profile_link)
        log_message(f"Profile link clicked for user: {username}")

        driver.execute_script("arguments[0].scrollIntoView(true);", profile_link)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'//a[@href="https://www.facebook.com/{username}"]')))
        driver.execute_script("arguments[0].click();", profile_link)
        log_message(f"Profile link clicked for user: {username}")
        # Wait for the profile page to load
        time.sleep(5)  # Adjust as necessary

        # Simulate liking a post (find a post and click the like button)
        # try:
        #     posts = WebDriverWait(driver, 20).until(
        #         EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "userContentWrapper")]'))
        #     )
        #     log_message(f"Found {len(posts)} posts on the profile page")

        #     # Randomly select a post to interact with
        #     post_to_like = random.choice(posts)
        #     like_button = post_to_like.find_element(By.XPATH, './/span[contains(@class, "pcp91wgn")]')

        #     # Scroll to the post and like it
        #     driver.execute_script("arguments[0].scrollIntoView(true);", post_to_like)
        #     time.sleep(1.5 + 0.5 * random.random())  # Simulating human delay before interaction
        #     like_button.click()
        #     log_message("Liked a post on the profile page")

        # except Exception as e:
        #     log_message(f"Exception occurred while liking a post: {e}")

        # Go back to the home page to perform the next search
        driver.get('https://www.facebook.com/')
        log_message("Navigated back to home page")

except Exception as e:
    log_message(f"Exception occurred: {e}")

finally:
    # Close the browser session
    # driver.quit()
    log_message("Browser session closed")
