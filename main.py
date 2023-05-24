from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obter_cadastro():
    username = input('Digite o CNPJ: ')
    password = input('Digite a senha: ')
    return (username, password)

login = obter_cadastro()
username = login[0]
password = login[1]

url = 'https://e-nfs.com.br/e-nfs_canoas/servlet/hlogin'

# Configurações do navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

def aguarda_carregamento_pagina():
    return WebDriverWait(driver, 30).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

def aguarda_elemento(by, value):
    return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((by, value)))

def clicar_elemento_por_texto(tag, texto):
    xpath = f"//{tag}[text()='{texto}']"
    clicar_elemento(By.XPATH, xpath)

def clicar_elemento(by, value):
    elemento = aguarda_elemento(by, value)
    elemento.click()

def preencher_login(username, password):
    username_input = aguarda_elemento(By.ID, 'vUSULOGIN')
    username_input.send_keys(username)

    password_input = aguarda_elemento(By.ID, 'vSENHA')
    password_input.send_keys(password)

preencher_login(username, password)
clicar_elemento(By.ID, 'BUTTON1')

clicar_elemento(By.ID, 'span_vVNOVO')

""" IDs para continuar o script
id_campo cliente == vCTBCPFCNPJ
id_local_cliente == vNFSLOCPRESTSRV
id_botao_avançar == BTNAVANCAR """

input("Pressione Enter para sair...")
driver.quit()