from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException






driver = webdriver.Edge() 
wait = WebDriverWait(driver, 10)

# Open the webpage
driver.get("https://domainnamestat.com/statistics/tldtype/all")

# Wait for 10 seconds
time.sleep(5)

# Save the current page before the loop
#current_page_data = driver.page_source

#with open("output.txt", "w") as file:
#    file.write(current_page_data)

# Rest of your code...

# Find the button element

# Define the number of times to click the button
num_clicks = 160

# Loop through the desired number of clicks
for i in range(num_clicks):
    try:
        # Wait for the element to be present 
        #element = wait.until(EC.presence_of_element_located((By.XPATH, f"//a[@data-dt-idx='{i+1}']")))
        #driver.execute_script("arguments[0].click();", element)
        # Delay to allow the new tab to fully load
        next_button = driver.find_element(By.ID, "top-50-tlds-breakdown-table_next")
        driver.execute_script("arguments[0].click();", next_button)

        time.sleep(5)
        tab_data = driver.page_source
    ium
        # Save the tab_data to a new output file
        with open(f"output{i+1}.txt", "w") as file:
            file.write(tab_data)

    except TimeoutException:
        next_button = driver.find_element(By.XPATH, "//a[text()='Next']")
        next_button.click() 
    
   # Close the new tab

# Close the browser
driver.quit()