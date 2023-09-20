from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--window-size=1920,1080')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/116.0.0.0 Safari/537.36')
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.implicitly_wait(10)
    driver.get("https://www.olx.ua/")

    EMAIL_INPUT = ("xpath", "//input[@name='username']")
    PASSWORD_INPUT = ("xpath", "//input[@name='password']")
    IN_BUTTON = ("xpath", "//button[@class='css-ypypxs']")

    driver.find_element(*EMAIL_INPUT).send_keys("ototototo923@gmail.com")
    driver.find_element(*PASSWORD_INPUT).send_keys("QWe123456789!")
    driver.find_element(*IN_BUTTON).click()

    count = 1
    while count < 11:

        driver.get("https://www.olx.ua/")

        items = driver.find_elements('class name', "mheight")
        items[0].click()

        driver.find_element('xpath', "//button[@data-cy='ad-contact-message-button']").click()
        input_field = driver.find_element('class name', "css-1kjjac5")
        input_field.clear()
        input_field.send_keys("Доброго Дня")
        driver.find_element('class name', "css-9x8rrm").click()

        time.sleep(10)

        link_element = driver.find_element('xpath', "//a[@name='user_ads']")
        href_value = link_element.get_attribute("href")

        user_link = f"({count}. {href_value})"
        with open("list_users.txt", "a") as file:
            file.write(user_link + "\n")

        count += 1

except Exception as ex:
    print(ex)
finally:
    driver.close()
