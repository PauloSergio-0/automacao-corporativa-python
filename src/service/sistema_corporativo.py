from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
import time
import os

class Sistema:
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    
    def acessar_site(self):

        load_dotenv(".\\keys_corporativas.env")

        

        self.driver.get(os.getenv("PORTAL"))
        self.driver.maximize_window()

        usuario = self.driver.find_element(By.ID,"username")
        usuario.send_keys(os.getenv("USERNAME"), Keys.ARROW_DOWN)

        senha = self.driver.find_element(By.ID,"password")
        senha.send_keys(os.getenv("PASSWORD"), Keys.ARROW_DOWN)

        self.driver.find_element(By.ID, "kc-login").click()

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, os.getenv("PORTAL_NACIONAL") )
            )
        ).click()


    def pagina_consulta(self):
            consulta = self.wait.until(
                EC.element_to_be_clickable(
                    (  By.XPATH, os.getenv("CONSULTA") )
                )
            )

            self.wait.until(
                EC.invisibility_of_element_located(
                    (By.CLASS_NAME, "background")
                )
            )

            consulta.click()

    def consultar(self,id_person):
        try:

            entrada_consulta = self.wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "mat-input-4")
                )
            )
            entrada_consulta.send_keys(id_person, Keys.ARROW_DOWN)

            self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, os.getenv("REALIZAR_CONSULTA"))
                )
            ).click()

            situacao = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, os.getenv("SITUACAO"))
                )
            )


            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, os.getenv("EXPANDIR_CONSULTA"))
                )
            )

            expandir = self.driver.find_element(
                By.XPATH,
                os.getenv("EXPANDIR_CONSULTA")
            )

            self.driver.execute_script(
                "arguments[0].click();",
                expandir
            )

            # ASSINATURA
            assinatura = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR,
                    os.getenv("ASSINATURA"))
                )
            ).text.strip()

            # DIGITAL
            digital = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR,
                    os.getenv("DIGITAL"))
                )
            ).text.strip()

            # FOTO
            foto = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR,
                    os.getenv("FOTO"))
                )
            ).text.strip()
        except TimeoutException:
            situacao = foto = assinatura = digital = "não encontrado"
        self.limpar_Consulta()
        return {"Ele": id_person, "situacao": situacao, "digital": digital, "foto": foto, "assinatural": assinatura}

    def limpar_Consulta(self):
        
        self.wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "mat-input-4")
                )
        ).clear()
        
        
    
    def fechar(self):
        self.driver.quit()
