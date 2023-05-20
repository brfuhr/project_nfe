from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define a URL
url = "https://www.e-nfs.com.br/e-nfs_canoas/portal/"

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

# Clica no link "Login Empresa / Autônomo"
link_login = driver.find_element(By.LINK_TEXT, "Login Empresa / Autônomo")
link_login.click()

# Insere o nome de usuário
username = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'USULOGIN')))
username.send_keys("_")

# Insere a senha
password = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'USUPASSWD')))
password.send_keys("_")

# Clica no botão de login
botao_login = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-signin')))
botao_login.click()

# Aguarda a interrupção manual para encerrar o programa
while True:
    pass

# O navegador será encerrado somente após a interrupção manual
driver.quit()