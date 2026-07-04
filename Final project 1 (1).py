from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

driver = webdriver.Firefox()
driver.get("https://www.amazon.in")
wait = WebDriverWait(driver, 60)

# Search
search = wait.until(
    EC.element_to_be_clickable(
        (By.ID, 'twotabsearchtextbox')
    )
)
time.sleep(3)
search.send_keys("Book")
search.click()
time.sleep(2)
search.send_keys(Keys.RETURN)

time.sleep(5)

# Get all Add to cart buttons
buttons = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, '//button[contains(., "Add to cart")]')
    )
)
print("Number of products found:", len(buttons))

# Choose random product
random_button = buttons[1]

# Scroll selected button into view
driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    random_button
)

time.sleep(2)


# Click selected product
driver.execute_script(
    "arguments[0].click();",
    random_button
)

time.sleep(5)
print("✅ Random book added to cart")
input("Press Enter to close...")
driver.quit()