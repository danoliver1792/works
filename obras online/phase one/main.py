from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pyautogui as pg

# defining the service with the compatible version of ChromeDriver
service = Service(ChromeDriverManager(version="latest").install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.obrasonline.com.br/')
driver.maximize_window()
sleep(2)

# logging in
login = ''
password = ''

xpath_button_login = '//*[@id="__next"]/div[1]/div/div[2]/div/div/nav/ul/li[7]/a'
xpath_login = '//*[@id="Email"]'
xpath_password = '//*[@id="Senha"]'
xpath_enter = '//*[@id="form"]/div[3]/button'

driver.find_element(By.XPATH, xpath_button_login).click()
sleep(3)
driver.find_element(By.XPATH, xpath_login).send_keys(login)
sleep(3)
driver.find_element(By.XPATH, xpath_password).send_keys(password)
sleep(3)
driver.find_element(By.XPATH, xpath_enter).click()
sleep(3)

# skip form
xpath_form = '//*[@id="panelFormulario"]/div/div[1]/div[2]/img'
driver.find_element(By.XPATH, xpath_form).click()
sleep(5)

# using the credits
xpath_credit = '//*[@id="cabecalho"]/div/ul[1]/li[4]/a'
xpath_use_credit = '//*[@id="ctl00_linkPesquisarObras"]'
driver.find_element(By.XPATH, xpath_credit).click()
sleep(2)
driver.find_element(By.XPATH, xpath_use_credit).click()
sleep(5)

# Choose by unused credits
xpath_unused_credit = '//*[@id="ctl00_ContentPlaceHolderPrincipal_filtroDeObras_containerCreditosUtilizado"]/span/div' \
                      '/div[1]/div/div '
driver.find_element(By.XPATH, xpath_unused_credit).click()
sleep(1)
pg.press('Down')
sleep(1)
pg.press('Enter')
sleep(1)

# using the filters

# "Entidade"
xpath_entidade = '//*[@id="ctl00_ContentPlaceHolderPrincipal_filtroDeObras_containerEntidadeEmpresa"]/div/div[1]/input'
driver.find_element(By.XPATH, xpath_entidade).click()
sleep(2)

pg.write('Construtor')
sleep(2)
pg.press('Enter')
sleep(2)

pg.write('Empreendedor')
sleep(2)
pg.press('Enter')
sleep(2)

pg.write('Esc')
sleep(2)
pg.press('Enter')
sleep(2)

pg.write('Gerenciadora')
sleep(2)
pg.press('Enter')
sleep(2)

pg.write('Incorporadora')
sleep(2)
pg.press('Enter')
sleep(2)

# "Tipo de Obra"
pg.press('Tab')
sleep(1)
pg.press('Tab')
sleep(1)

pg.write('Residencial')
sleep(2)
pg.press('Enter')
sleep(2)

pg.write('Comercial')
sleep(2)
pg.press('Enter')
sleep(2)

pg.write('Industrial')
sleep(2)
pg.press('Enter')
sleep(2)

# "UF"
xpath_uf = '//*[@id="ctl00_ContentPlaceHolderPrincipal_filtroDeObras_containerPesquisaDeObras"]/div[' \
           '2]/div/div/fieldset/div/div[5]/div[1]/input '

driver.find_element(By.XPATH, xpath_uf).click()
sleep(2)
pg.write('Santa Catarina')
sleep(2)
pg.press('Enter')
sleep(2)
pg.write('Parana')
sleep(2)
pg.press('Enter')
sleep(2)
pg.press('Esc')
sleep(2)

# searching
xpath_search = '//*[@id="ctl00_ContentPlaceHolderPrincipal_buttonPesquisar"]'
driver.find_element(By.XPATH, xpath_search).click()
sleep(10)

# searching the works
for n in range(1, 51):
    xpath_works = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[1]/div/div[' \
                  f'14]/button[2] '
    xpath_page = '/html/body/form/div[7]/div[2]/div/div/div/div/div/div[5]/div/div/ul/li[23]/a'
    driver.find_element(By.XPATH, xpath_works).click()
    sleep(5)
    pg.press('Tab')
    sleep(5)
    pg.press('Enter')
    sleep(5)
    pg.press('Enter')
    sleep(5)

    # skip the page when the robot reaches the last one
    if n == 50:
        driver.find_element(By.XPATH, xpath_page).click()
        continue

driver.quit()

