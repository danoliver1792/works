import tkinter
import openpyxl as op
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from tkinter import *
from PIL import Image, ImageTk


def search():
    try:
        # loading the XLSX file, selecting the worksheet and column A
        file_xlsx = r'C:\Users\danrl\Documents\PythonAgile\Pesquisa\price.xlsx'
        sheet_xlsx = 'Plan1'
        column = 'A'

        workbook = op.load_workbook(file_xlsx)
        sheet = workbook[sheet_xlsx]

        # configuring the Chrome Driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # collecting OLX data
        for i, row_cell in enumerate(sheet[column], start=1):
            value_cell = row_cell.value

            driver.get('https://www.olx.com.br/')
            driver.maximize_window()
            sleep(5)

            xpath_search_olx = '/html/body/div[1]/header/nav/div/div[1]/div[2]/div/div[1]/div/div/div/span/input'
            xpath_search_olx_click = '/html/body/div[1]/header/nav/div/div[1]/div[2]/div/button'
            xpath_product_olx = '/html/body/div[1]/div/main/div[1]/div[2]/main/div[3]/section/div[2]/div[1]/div[1]'
            xpath_price_olx = '/html/body/div[1]/div/main/div[1]/div[2]/main/div[3]/section/div[2]/div[1]/div[2]/h3'

            driver.find_element(By.XPATH, xpath_search_olx).send_keys(value_cell)
            sleep(5)
            driver.find_element(By.XPATH, xpath_search_olx_click).click()
            sleep(5)
            product_olx = driver.find_element(By.XPATH, xpath_product_olx).text
            sleep(5)
            price_olx = driver.find_element(By.XPATH, xpath_price_olx).text
            sleep(5)

            sheet[f'B{i}'] = product_olx
            sheet[f'C{i}'] = price_olx

        # collecting Mercado Libre data
        for i, row_cell in enumerate(sheet[column], start=1):
            value_cell = row_cell.value

            driver.get('https://www.mercadolivre.com.br/')
            driver.maximize_window()
            sleep(5)

            xpath_search_ml = '/html/body/header/div/div[2]/form/input'
            xpath_search_ml_click = '/html/body/header/div/div[2]/form/button'
            xpath_product_ml = '/html/body/main/div/div[2]/section/ol/li[1]/div/div/div[2]/div[1]/a/h2'
            xpath_price_ml = ('/html/body/main/div/div[2]/section/ol/li[1]/div/div/div[2]/div[2]/div[1]/div['
                              '1]/div/div/div')

            driver.find_element(By.XPATH, xpath_search_ml).send_keys(value_cell)
            sleep(5)
            driver.find_element(By.XPATH, xpath_search_ml_click).click()
            sleep(5)
            product_ml = driver.find_element(By.XPATH, xpath_product_ml).text
            sleep(5)
            price_ml = driver.find_element(By.XPATH, xpath_price_ml).text
            sleep(5)

            sheet[f'E{i}'] = product_ml
            sheet[f'F{i}'] = price_ml

        # collecting Smart Center data
        for i, row_cell in enumerate(sheet[column], start=1):
            value_cell = row_cell.value
            text_smart = value_cell.split()

            xpath_product_smart = '//*[@id="gallery-layout-container"]/div[1]/section/a/article/div[4]/h3/span'
            xpath_price_smart = ('//*[@id="gallery-layout-container"]/div[1]/section/a/article/div[6]/div/div['
                                 '1]/span/span')

            if len(text_smart) == 2:
                url = f'https://www.espacosmart.com.br/{text_smart[0]}%20{text_smart[1]}?_q={text_smart[0]}%20{text_smart[1]}&map=ft'
                driver.get(url)
                sleep(10)

                product_smart = driver.find_element(By.XPATH, xpath_product_smart).text
                price_smart = driver.find_element(By.XPATH, xpath_price_smart).text

                sheet[f'H{i}'] = product_smart
                sheet[f'I{i}'] = price_smart

            elif len(text_smart) == 3:
                url = f'https://www.espacosmart.com.br/{text_smart[0]}%20{text_smart[1]}%20{text_smart[2]}?_q={text_smart[0]}%20{text_smart[1]}%20{text_smart[2]}&map=ft'
                driver.get(url)
                sleep(10)

                product_smart = driver.find_element(By.XPATH, xpath_product_smart).text
                price_smart = driver.find_element(By.XPATH, xpath_price_smart).text

                sheet[f'H{i}'] = product_smart
                sheet[f'I{i}'] = price_smart

            else:
                driver.quit()
                print('Page not found...')

            workbook.save(file_xlsx)
    except Exception as e:
        print(f'Error: {e}')


# configuring screen
screen = tkinter.Tk()
screen.title('Search Price')

# frame that will contain the image
frame = tkinter.Frame(screen, height=100, width=50)
frame.pack()

# loading image
image = Image.open(r'C:\Users\danrl\Documents\PythonAgile\Pesquisa\logo png.png')
photo = ImageTk.PhotoImage(image)

# label widget to display the image
image_label = tkinter.Label(frame, image=photo)
image_label.photo = photo
image_label.pack()

# creating button
button = tkinter.Button(screen, text='Search', command=search, font='Ivy 8 bold', bg='#ff6600', fg='#feffff',
                        relief=RAISED, overrelief=RIDGE)
button.place(x=178, y=150)

screen.geometry('400x200')
screen.mainloop()
