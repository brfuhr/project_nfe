from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obter_cadastro():
    username = input("Digite o CNPJ: ")
    password = input("Digite a senha: ")
    return (username, password)

# Obtém o login antes de abrir o navegador
login = obter_cadastro()
username = login[0]
password = login[1]

# Define a URL
url = "https://www.e-nfs.com.br/e-nfs_canoas/portal/"

# https://e-nfs.com.br/e-nfs_canoas/servlet/hlogin alterar pra esse link 

# Configurações do navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Inicializa o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Aguarda o carregamento completo da página
def wait_for_page_load():
        WebDriverWait(driver, 30).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

# Aguarda elemento clicável
def wait_for_element(by, value):
    try:
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((by, value)))
    except:
        print("Elemento não encontrado ou não clicável.")

# Clicar no elemento pelo texto
def clicar_elemento_por_texto(tag, texto):
    xpath = f"//{tag}[text()='{texto}']"
    clicar_elemento(xpath)

# Clicar em um elemento pelo xpath
def clicar_elemento(xpath):
        elemento = wait_for_element(By.XPATH, xpath)
        elemento.click()

def preencher_login(username, password):
    username_input = wait_for_element(By.ID, 'USULOGIN')
    username_input.send_keys(username)

    password_input = wait_for_element(By.ID, 'USUPASSWD')
    password_input.send_keys(password)

    botao_login = wait_for_element(By.XPATH, '//button[contains(text(), "Acessar")]')
    botao_login.click()

# Efetua o login
clicar_elemento_por_texto("a", "Login Empresa / Autônomo")

preencher_login(username, password)

input("Pressione Enter para sair...")

driver.quit()