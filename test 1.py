from selenium import webdriver
import time


driver = webdriver.Chrome()

# Common device viewports (width x height)
viewports = [
    (1920, 1080),   # Full HD Desktop
    (1366, 768),    # Laptop
    (1440, 900),    # MacBook Pro
    (1536, 864),    # Desktop HD+
    (1280, 720),    # HD Ready
    (1024, 768),    # iPad (Landscape)
    (768, 1024),    # iPad (Portrait)
    (414, 896),     # iPhone XR/11/11 Pro Max
    (375, 812),     # iPhone X/XS
    (375, 667),     # iPhone 6/7/8
    (360, 800),     # Android large phone
    (320, 568),     # iPhone SE
]

driver.get('https://www.imdb.com/')

try:
    for width, height in viewports:
        print(f"Setting window size to: {width}x{height}")
        driver.set_window_size(width, height)
        time.sleep(2)  # Pause to observe each viewport

finally:
    print("Closing browser...")
    driver.quit()

print ('hello world')

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.imdb.com/")
driver.maximize_window()
time.sleep(4)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("Scrolled down")
time.sleep(4)

driver.execute_script("window.scrollTo(0, 0);")
print("Scrolled up")
time.sleep(4)

driver.execute_script("document.body.style.zoom='125%'")
print("Zoomed In")
time.sleep(4)

driver.execute_script("document.body.style.zoom='75%'")
print("Zoomed Out")
time.sleep(4)

driver.execute_script("document.body.style.zoom='100%'")
print("Reset Zoom")
time.sleep(4)

driver.quit()