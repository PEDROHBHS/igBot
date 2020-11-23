from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
       self.username = username
       self.password = password
       self.driver = webdriver.Firefox(executable_path=r"C:\Users\pepeb\Desktop\driver\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        
        inputUsuario = driver.find_element_by_xpath("//input[@name='username']")
        inputUsuario.click()
        inputUsuario.clear()
        inputUsuario.send_keys(self.username)

        inputSenha = driver.find_element_by_xpath("//input[@name='password']")
        inputSenha.click()
        inputSenha.clear()
        inputSenha.send_keys(self.password)
        inputSenha.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comentar_em_fotos()

    @staticmethod
    def digite_como_uma_pessoa(frase, ondeDigitar):
        for letra in frase:
            ondeDigitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comentar_em_fotos(self):
        driver = self.driver
        driver.get("link") 

        for i in range (1,70):
            try:
                comentarios = ["Olá", "Linde", "Ulhull"]
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2,5))
                self.digite_como_uma_pessoa(random.choice(comentarios),campo_comentario)
                time.sleep(random.randint(30,100))
                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                time.sleep(5)
            except Exception as e:
                print(e)
                time.sleep(5)


phBot = InstagramBot('user','password')
phBot.login()
