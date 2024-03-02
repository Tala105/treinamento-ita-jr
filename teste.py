from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("-headless") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("----window-size=1920,1080")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up Chrome webdriver through webdriver_manager
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Choose English language
english_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
english_button.click()
time.sleep(2)

while True:
    running = True
    start_time = time.time()
    while running:
        golden_cookie = driver.find_element(By.ID, "goldenCookie")
        if golden_cookie.is_displayed():
            golden_cookie.click()
            effect = golden_cookie.get_attribute("title")
            print("Golden Cookie Effect:", effect)
        cookie = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "bigCookie")))
        cookie.click()
        
        upgrades = driver.find_elements(By.CSS_SELECTOR, ".upgrade.enabled")
        if upgrades:
            for upgrade in upgrades:
                upgrade.click()
        
        buildings = driver.find_elements(By.CSS_SELECTOR, ".product.enabled")
        if buildings:
            for building in buildings:
                if "enabled" in building.get_attribute("class"):
                    cost = int(building.find_element(By.CSS_SELECTOR, ".content .price").text.replace(",", ""))
                    cookies = int(driver.find_element(By.ID, "cookies").text.replace(",", "").split(" ")[0])
                    if cookies > cost:
                        building.click()

                current_time = time.time()
                if current_time - start_time >= 10:
                    cookies = driver.find_element(By.ID, "cookies")
                    print(f"{cookies.text}\nElapsed Time = {current_time}s")
                    start_time = current_time
# Close the browser
driver.quit()