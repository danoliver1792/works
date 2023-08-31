from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import csv

service = Service(ChromeDriverManager(version='latest').install())
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

# find and click element using XPATH
xpath_work_menu = '//*[@id="cabecalho"]/div/ul[1]/li[4]'
driver.find_element(By.XPATH, xpath_work_menu).click()
sleep(3)

# clicking used credits
xpath_used_credits = '//*[@id="ctl00_liCreditosUtilizados"]'
driver.find_element(By.XPATH, xpath_used_credits).click()
sleep(3)

# CSV file creation
csv_file = r'C:\Users\danrl\OneDrive\Python\Obras Online\Results\obras_online4.csv'

with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Empresa', 'Entidade', 'Nome da Obra', 'Empreendedor', 'Contato', 'Cargo', 'Telefones', 'e-mail',
                     'Endereco', 'Numero', 'Cidade', 'uf', 'previsao de termino', 'Sub-setor', 'Especificacao',
                     'Investimento', 'Valor', 'Area m²'])

    for c in range(1, 33):
        xpath_page = '/html/body/form/div[7]/div[2]/div/div/div/div/div/div[5]/div/div/ul/li[23]/a'
        driver.find_element(By.XPATH, xpath_page).click()
        sleep(10)

    i = 1

    while i < 77:
        for n in range(1, 51):
            # click on the magnifying glass
            xpath_works = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[1]/div/div[' \
                          f'14]/button[3] '
            driver.find_element(By.XPATH, xpath_works).click()
            sleep(5)

            # xpath to the data
            xpath_empresa = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[3]/div[' \
                            f'3]/div/div[3]/div[1]/span '
            xpath_entidade = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[3]/div[' \
                             f'3]/div/div[4]/span '
            xpath_nome_obra = (f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div['
                               f'1]/div/div[6]/span[2]')
            xpath_empreendedor = (f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div['
                                  f'1]/div/div[7]/span[2]')
            xpath_contato = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[3]/div[' \
                            f'3]/div/div[5]/span '
            xpath_cargo = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[3]/div[' \
                          f'3]/div/div[6]/span '
            xpath_telefones = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[3]/div[' \
                              f'3]/div/div[7] '
            xpath_email = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[3]/div[' \
                          f'3]/div/div[8]/a '
            xpath_endereco = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[2]/div[' \
                             f'3]/div[1]/span[2] '
            xpath_numero = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[2]/div[' \
                           f'3]/div[1]/span[3] '
            xpath_cidade = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[2]/div[' \
                           f'3]/div[4]/div[1]/span[2] '
            xpath_uf = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[2]/div[3]/div[' \
                       f'4]/div[2]/span[2] '
            xpath_previsao = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[2]/div[' \
                             f'2]/div[5]/span[2] '
            xpath_sub = (f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[2]/div['
                         f'4]/div[1]/span[2]')
            xpath_especificacao = (f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div['
                                   f'2]/div[4]/div[2]/div/span[2]')
            xpath_investimento = (f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div['
                                  f'2]/div[5]/div[1]/div[1]/span[2]')
            xpath_valor = (f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[2]/div['
                           f'5]/div[1]/div[2]/span[2]')
            xpath_area = (f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[4]/div/div[{n}]/div/div[2]/div['
                          f'5]/div[2]/div[1]/span[2]')
            xpath_pagina = f'/html/body/form/div[7]/div[2]/div/div/div/div/div/div[5]/div/div/ul/li[23]/a'

            empresa = driver.find_element(By.XPATH, xpath_empresa).text
            entidade = driver.find_element(By.XPATH, xpath_entidade).text
            nome_obra = driver.find_element(By.XPATH, xpath_nome_obra).text
            empreendedor = driver.find_element(By.XPATH, xpath_empreendedor).text
            contato = driver.find_element(By.XPATH, xpath_contato).text
            cargo = driver.find_element(By.XPATH, xpath_cargo).text
            telefones = driver.find_element(By.XPATH, xpath_telefones).text
            email = driver.find_element(By.XPATH, xpath_email).text
            endereco = driver.find_element(By.XPATH, xpath_endereco).text
            numero = driver.find_element(By.XPATH, xpath_numero).text
            cidade = driver.find_element(By.XPATH, xpath_cidade).text
            uf = driver.find_element(By.XPATH, xpath_uf).text
            previsao = driver.find_element(By.XPATH, xpath_previsao).text
            sub = driver.find_element(By.XPATH, xpath_sub).text
            especificacao = driver.find_element(By.XPATH, xpath_especificacao).text
            investimento = driver.find_element(By.XPATH, xpath_investimento).text
            valor = driver.find_element(By.XPATH, xpath_valor).text
            area = driver.find_element(By.XPATH, xpath_area).text

            writer.writerow([empresa, entidade, nome_obra, empreendedor, contato, cargo, telefones, email, endereco,
                             numero, cidade, uf, previsao, sub, especificacao, investimento, valor, area])

            sleep(8)

        driver.find_element(By.XPATH, xpath_pagina).click()

        sleep(10)

        i += 1

driver.quit()
