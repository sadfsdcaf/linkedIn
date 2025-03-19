import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def process_contacts(file_path):
    try:
        print(f"Attempting to read: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.linkedin.com/login")
        time.sleep(30)  # Pause to manually log in

        for line in lines:
            name = line.strip()
            if name:
                print(f"Searching for: {name}")
                driver.get("https://www.linkedin.com/search/results/people/")
                time.sleep(3)

                search_box = driver.find_element(By.XPATH, '//input[contains(@placeholder, "Search")]')
                search_box.send_keys(name)
                search_box.send_keys(Keys.RETURN)
                time.sleep(3)

                try:
                    connect_buttons = driver.find_elements(By.XPATH, '//span[contains(text(), "Connect")]/ancestor::button')
                    if connect_buttons:
                        connect_buttons[0].click()
                        time.sleep(2)

                        send_button = driver.find_element(By.XPATH, '//button[contains(@aria-label, "Send now")]')
                        send_button.click()
                        print(f"Connection request sent to {name}.")
                        time.sleep(5)
                    else:
                        print(f"No connect button found for {name}.")
                except Exception as e:
                    print(f"Could not connect with {name}: {e}")

        print("Process complete.")
        driver.quit()

    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    process_contacts("linkedin.txt")
