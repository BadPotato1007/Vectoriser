from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import time
import os
chromedriver_autoinstaller.install()
# Set Chrome options to enable incognito mode
chrome_options = Options()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--headless')


driver = webdriver.Chrome(options=chrome_options)

try:
    print("please enter the name of your file with the extension")
    file_name = input("PS: it must be in the same directory as this file: ")
    print()
    mode = input('''Please enter render mode:   (just the number please!)
          [1] Quick Render --> Recommended for most images
          [2] Normal Render  --> Use if Quick render gives incomplete results
          [3] Full Render  --> Only use if both renders give incomplete results
          ''')
    if mode == '1':
        time_to_sleep = 15
    elif mode == '2':
        time_to_sleep = 30
    elif mode == '3':
        time_to_sleep = 70
    wait = WebDriverWait(driver, 1000)

    driver.get("https://www.vectorizer.io/")
    upload_file = os.path.abspath(file_name)

    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(upload_file)
    time.sleep(int(time_to_sleep))
    elem = wait.until(EC.visibility_of_element_located((By.ID, 'outputsvg')))
    source_code = elem.get_attribute("outerHTML")
    
    
    fn = file_name.split('.')
    filename = fn[0] + '.svg'
    
    
    
    with open(filename, 'x') as f:
        f.write(source_code)
    print("Done! please check the file")


finally:
    # Close the browser
    driver.quit()
