# program with simple interface. Customer searches and retrieves the 60 results on Google Shopping

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from tkinter import *
from tkinter import Tk
import pyautogui as pg
import csv

color1 = '#f0f3f5'
color2 = '#feffff'
color3 = '#ff6600'
color4 = '#38576b'
color5 = '#403d3d'

window = Tk()
window.title('')
window.geometry('310x300')
window.configure(background=color3)
window.resizable(width=FALSE, height=FALSE)


def search_google():
    search = e_name.get()
    sleep(2)

    service = Service(ChromeDriverManager(version='latest').install())
    driver = webdriver.Chrome(service=service)

    driver.get('https://www.google.com.br/')
    driver.maximize_window()
    sleep(2)

    xpath_search = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea'
    xpath_button_search = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]'
    xpath_shopping = '/html/body/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[2]'

    driver.find_element(By.XPATH, xpath_search).send_keys(search)
    sleep(2)
    pg.press('Esc')
    sleep(3)
    driver.find_element(By.XPATH, xpath_button_search).click()
    sleep(5)
    driver.find_element(By.XPATH, xpath_shopping).click()
    sleep(5)

    csv_file = fr'C:\Users\danrl\OneDrive\Python\Pesquisa Precos\results\{search}.csv'

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Nome', 'Preco'])

        for n in range(1, 60):
            xpath_product = f'/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[{n}]/div[' \
                            f'1]/div[2]/span'
            xpath_store = f'/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[{n}]/div[1]/div[' \
                          f'2]/div[2]'

            product = driver.find_element(By.XPATH, xpath_product).text
            store = driver.find_element(By.XPATH, xpath_store).text

            writer.writerow([product, store])


frame_up = Frame(window, width=310, height=50, bg=color2, relief='flat')
frame_up.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_down = Frame(window, width=310, height=250, bg=color2, relief='flat')
frame_down.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

l_name = Label(frame_up, text='Pesquisa no Google', anchor=NE, font='Ivy 25', bg=color2, fg=color5)
l_name.place(x=5, y=5)

l_row = Label(frame_up, text='', width=275, anchor=NW, font='Ivy 1', fg=color5)
l_row.place(x=10, y=45)

e_name = Entry(frame_down, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
e_name.place(x=14, y=50)

b_submit = Button(frame_down, command=search_google, text='Pesquisar', width=39, height=2, font='Ivy 8 bold', bg=color3,
                  fg=color2, relief=RAISED, overrelief=RIDGE)
b_submit.place(x=15, y=150)

window.mainloop()
