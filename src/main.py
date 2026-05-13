from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import os


load_dotenv(".\\keys_corporativas.env")

driver = webdriver.Chrome()

# driver.get("https://google.com")



driver.get(os.getenv("PORTAL"))
driver.maximize_window()

usuario = driver.find_element(By.ID,"username")
usuario.send_keys(os.getenv("USERNAME"), Keys.ARROW_DOWN)

senha = driver.find_element(By.ID,"password")
senha.send_keys(os.getenv("PASSWORD"), Keys.ARROW_DOWN)

botao_login = driver.find_element(By.ID, "kc-login").click()

wait = WebDriverWait(driver, 20)
acesso_site = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, os.getenv("PORTAL_NACIONAL"))
    )
)

acesso_site.click()

consulta = wait.until(
    EC.element_to_be_clickable(
        (  By.XPATH,
            '//a[contains(., " ")]')
    )
)

consulta.click()

time.sleep(10)

driver.quit()
