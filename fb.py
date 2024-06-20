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

    # Directly navigate to the profile URL
    profile_url = 'https://www.facebook.com/mg.yo.374'
    log_message(f"Directly navigating to profile URL: {profile_url}")
    driver.get(profile_url)

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

except Exception as e:
    log_message(f"Exception occurred: {e}")

finally:
    # Close the browser session
    # driver.quit()
    log_message("Browser session closed")
