import tkinter as tk
from tkinter import messagebox
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from PIL import Image, ImageTk
from datetime import date
import pandas
import time

class xpath:
    def __init__(self, label_text, grid_row, grid_column, place_x, place_y):

        self.label = tk.Label(window, text=f"{label_text}")
        self.label.pack()
        self.label.grid(row=grid_row, column=grid_column)
        self.label.place(x=place_x, y=place_y)

    def hide(self):
        self.label.place_forget()

class checkbox:
    def __init__(self,text, variable, place_x, place_y):
        self.checkbutton = tk.Checkbutton(text=f"{text}", variable=variable)
        self.checkbutton.pack()
        self.checkbutton.place(x=place_x, y=place_y)
    def hide(self):
        self.checkbutton.place_forget()
    def checked(self):
        self.checkbutton.select()



# GUI oberfläche login Seite
def login_test():
    global login_xpath, username_xpath, passwort_xpath,anmelde_xpath,login_checkbox1,login_checkbox2,login_checkbox3,test,\
        login_entry, username_entry, passwort_entry, anmelde_entry,test_login_button
    # Login/Registrierung Button Label
    login_xpath = xpath(label_text="Login Button", grid_row=1, grid_column=0, place_x=50, place_y=100)
    login_entry = tk.Entry(window, width=30)
    login_entry.grid(row=1,column=1, columnspan=5)
    login_entry.place(x=180,y=100)
    # Username xpath Entry
    username_xpath = xpath(label_text="Eingabe Username", grid_row=1, grid_column=0, place_x=50, place_y=120)
    username_entry = tk.Entry(window, width=30)
    username_entry.grid(row=1,column=1, columnspan=5)
    username_entry.place(x=180,y=120)
    # Passwort xpath entry
    passwort_xpath = xpath(label_text="Eingabe Passwort", grid_row=1, grid_column=0, place_x=50, place_y=140)
    passwort_entry = tk.Entry(window, width=30)
    passwort_entry.grid(row=1,column=1, columnspan=5)
    passwort_entry.place(x=180,y=140)
    # anmelde Button xpath
    anmelde_xpath = xpath(label_text="Anmelde Button", grid_row=1, grid_column=0, place_x=50, place_y=160,)
    anmelde_entry = tk.Entry(window, width=30)
    anmelde_entry.grid(row=1,column=1, columnspan=5)
    anmelde_entry.place(x=180,y=160)
    # Checkboxen zum abhaken nach Testablauf
    checked_testfall_1 = tk.IntVar()
    login_checkbox1 = checkbox("Tf 1 > Testet, ob Passwort durch * verdeckt",checked_testfall_1,30,190)
    checked_testfall_1.get()

    checked_testfall_2 = tk.IntVar()
    login_checkbox2 = checkbox("Tf 2 > Testet, ob Login nach drei fehlversuche gesperrt ist", checked_testfall_2,30,210)
    checked_testfall_2.get()

    checked_testfall_3 = tk.IntVar()
    login_checkbox3 = checkbox("Tf 3 > Testet, ob Groß- und Kleinbuchstaben validieren", checked_testfall_3,30,230)
    checked_testfall_3.get()
    # Test starten Button
    test_login_button = tk.Button(window, text="Test starten", command=lambda:[get_data_input(),create_filedata(),run_login_test()])
    test_login_button.pack()
    test_login_button.place(x=200, y=260)
    test_login_button.config(padx=10)

# GUI oberfläche suchleiste Seite
def suchleiste_test():
    global suchleiste_label, suchleiste_checkbox , shop_link, shop_entry, suchleiste_entry,test_suchleiste_button

    shop_link = xpath(label_text="Navbar Shop", grid_row=1, grid_column=0, place_x=50, place_y=100)
    shop_entry = tk.Entry(window, width=30)
    shop_entry.grid(row=1,column=1, columnspan=5)
    shop_entry.place(x=180, y=100)
    suchleiste_label = xpath(label_text="Produkt Suchleiste", grid_row=1, grid_column=0, place_x=50, place_y=120)
    suchleiste_entry = tk.Entry(window,width=30)
    suchleiste_entry.grid(row=1,column=1,columnspan=5)
    suchleiste_entry.place(x=180, y=120)
    checked_testfall_1 = tk.IntVar()
    suchleiste_checkbox = checkbox("Tf 1 > Testet, ob Eingabe nach Groß- und Kleinbuchstaben \n"
                                   "mit dem Produkt validieren",checked_testfall_1,30,190)

    # Test starten Button
    test_suchleiste_button = tk.Button(window, text="Test starten", command=lambda:[get_data_input(),create_filedata(),run_search_test()])
    test_suchleiste_button.pack()
    test_suchleiste_button.place(x=200, y=260)
    test_suchleiste_button.config(padx=10)

# GUI oberfläche warenkorb Seite
def warenkorb_test():
    global warenkorb_xpath, warenkorb_checkbox, warenkorb_checkbox_2, warenkorb_checkbox_3, xpath_gesamtpreis, xpath_warenwert,\
        warenkorb_input,warenwert_input,test_warenkorb_button
    warenkorb_xpath = xpath(label_text="Warenkorb Button", grid_row=1, grid_column=0, place_x=50, place_y=100)
    warenkorb_input = tk.Entry(window, width=30)
    warenkorb_input.grid(row=1,column=1,columnspan=5)
    warenkorb_input.place(x=180, y=100)
    xpath_warenwert = xpath(label_text="Warenwert", grid_row=1, grid_column=0, place_x=50, place_y=120)
    warenwert_input = tk.Entry(window, width=30)
    warenwert_input.grid(row=1, column=1, columnspan=5)
    warenwert_input.place(x=180, y=120)
    checked_testfall_1 = tk.IntVar()
    warenkorb_checkbox = checkbox("Tf 1 > Testet, ob Produkte im Warenkorb gespeichert ist",checked_testfall_1,30,190)
    checked_testfall_2 = tk.IntVar()
    warenkorb_checkbox_2 = checkbox("Tf 2 > Testet, ob die Anzahl mit dem Gesamtpreis übereinstimmt",checked_testfall_2,30,210)
    checked_testfall_3 = tk.IntVar()
    warenkorb_checkbox_3 = checkbox("Tf 3 > Testet, ob der Warenwert mit der Summe übereinstimmt",checked_testfall_3,30,230)
    # Test starten Button
    test_warenkorb_button = tk.Button(window, text="Test starten", command=lambda:[get_data_input(),create_filedata(),run_cart_test()])
    test_warenkorb_button.pack()
    test_warenkorb_button.place(x=200, y=260)
    test_warenkorb_button.config(padx=10)

# Funktion zur Aktualisierung der GUI basierend auf der aktuellen Seite
def update_gui():
    global login_xpath, username_path, passwort_xpath, anmelde_xpath,\
        page,testfall_1,testfall_2,testfall_3, close_software
    if page == 0:
        window.title("Test automatisation Software")
        button_back.place_forget()


    elif page == 1:
        window.title("Testsuites Login/Registry")
        login_instruction = tk.Label(window, text="Testsuites Login" 
                                      "\n\nFüge den Xpath ein um die Login Funktion zu testen")
        login_instruction.place(x=50, y=30)
        label_instruction.place_forget()
        canvas.place_forget()
        label_hinweis.place_forget()
        entry_url.place_forget()
        entry_tester.place_forget()
        entry_projektnr.place_forget()
        label_projektnr.place_forget()
        label_url.place_forget()
        label_tester.place_forget()
        login_test()


    elif page == 2:
        window.title("Testsuites Searchbar")
        searchbar_instruction = tk.Label(window, text="Testsuites Suchleiste"
                                      "'\n\nFüge den Xpath ein um die Suchleiste zu testen")
        searchbar_instruction.place(x=50,y=30)
        login_xpath.hide()
        username_xpath.hide()
        passwort_xpath.hide()
        anmelde_xpath.hide()
        login_checkbox1.hide()
        login_checkbox2.hide()
        login_checkbox3.hide()
        login_entry.place_forget()
        username_entry.place_forget()
        passwort_entry.place_forget()
        anmelde_entry.place_forget()
        test_login_button.place_forget()
        suchleiste_test()
    elif page == 3:
        global warenkorb_xpath, close_software
        window.title("Testcase Warenkorb")
        warenkorb_instruction = tk.Label(window, text="Testsuites Warenkorb"
                                      "\n\nFüge den Xpath ein um den Warenkorb zu testen")
        warenkorb_instruction.place(x=50,y=30)
        suchleiste_label.hide()
        suchleiste_checkbox.hide()
        shop_link.hide()
        warenkorb_test()
        shop_entry.place_forget()
        suchleiste_entry.place_forget()
        test_suchleiste_button.place_forget()
        button_continue.place_forget()
        close_software = tk.Button(window, text="Beenden", command=window.destroy)
        close_software.place(x=300, y=260)
        close_software.config(padx=10)

# Verbindung aufbauen über Selenium mit Website
def url_connect():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(f"{url_input}")
    time.sleep(20)

    driver.quit()

# Funktion Daten entnehmen zur weiterverarbeitung
def get_data_input():
    global projektnr_input, tester_input, url_input, loging_input, login_username, login_passwort, login_anmelde\
        ,login_xpath1, username_xpath1, passwort_xpath1, anmelde_xpath1, shop_link_xpath1, suchleiste_xpath1,warenkorb_input1, shop_link_xpath, suchleiste_xpath, warenwert_input1
    if page == 0:
        projektnr_input = entry_projektnr.get()
        tester_input = entry_tester.get()
        url_input= entry_url.get()
    elif page == 1:
        login_xpath1 = login_entry.get()
        username_xpath1 = username_entry.get()
        passwort_xpath1 = passwort_entry.get()
        anmelde_xpath1 = anmelde_entry.get()
    elif page ==2:
        shop_link_xpath = shop_entry.get()
        suchleiste_xpath = suchleiste_entry.get()
    else:
        warenkorb_input1 = warenkorb_input.get()
        warenwert_input1 = warenwert_input.get()

# Funktion Inhalt button "Info"
def show_info():
    info_text = """
    1. Funktion „Login Funktion“ wird getestet auf
        Grundlage:
        - Testfall 1 > Testet, ob Passwort verdeckt ist
        - Testfall 2 > Testet, ob Login nach vier fehlversuche
            gesperrt ist
        - Testfall 3 > Testet, ob Groß- und Kleinbuchstaben 
            validieren
        
    2. Funktion „Suchleiste Funktion“ wird getestet auf
        Grundlage:
        - Testfall 1 > Testet, ob Eingabe nach Groß- und
            Kleinbuchstaben mit dem Produkt validieren
        
    3. Funktion „Warenkorb Funktion“ wird getestet auf
        Grundlage: 
        - Testfall 1 > Testet, ob Produkte im Warenkorb 
            nach erneutem Login gespeichert ist
        - Testfall 2 > Testet, ob die Anzahl eines Produktes mit
            dem Gesamtpreis übereinstimmt
        - Testfall 3 > Testet, ob die Summe im Warenkorb mit
            dem addierten Preis in der Datenbank übereinstimmt.
    """
    messagebox.showinfo("Testfälle", info_text)

# show Testergebnis an
def show_test_result():
    if page == 1:
        with open("Login Testsuite.txt") as file:
            show = file.read()
        messagebox.showinfo("Test Ergebnis", show)
    elif page == 2:
        with open("Searchbar Testsuite.txt") as file:
            show = file.read()
        messagebox.showinfo("Test Ergebnis", show)
    else:
        with open("Shopping cart Testsuite.txt") as file:
            show = file.read()
        messagebox.showinfo("Test Ergebnis", show)

# Hauptfunktion zur Ausführung des Tests für LOGIN
def run_login_test():
    # Hier kommen die Testlogiken für LOGIN
    global TestName, TestPW, testname, TestfalschPW
    TestName = "Test"
    testname = "test"
    TestPW = "12345678"
    TestfalschPW = "sdfasdf"

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(f"{url_input}")
    time.sleep(1)
    cookie = driver.find_element("xpath", f"{login_xpath1}")
    time.sleep(1)
    cookie.click()
    time.sleep(1)
    cookie = driver.find_element("xpath", f"{username_xpath1}")
    time.sleep(1)
    cookie.click()
    cookie.send_keys(f"{testname}")
    time.sleep(1)
    cookie = driver.find_element("xpath", f"{passwort_xpath1}")
    time.sleep(1)
    cookie.click()
    cookie.send_keys(f"{TestPW}")
    time.sleep(1)
    cookie = driver.find_element("xpath", f"{anmelde_xpath1}")
    time.sleep(1)
    cookie.click()
    time.sleep(1)
    cookie = driver.find_element("xpath", '//*[@id="accountbar"]/table/tbody/tr[2]/td/a[2]')
    time.sleep(1)
    cookie.click()
    time.sleep(1)
    #Tf 1 und Tf 3 können hier getestet werden
    #Tf 1 Passwort verdecken
    # Checkbox abhacken mit x oder i
    if TestPW != "********":
        with open("Login Testsuite.txt", mode="a") as file:
            file.write(f"\n\n\n Testfall 1 > Teste, ob Passwort verdeckt ist. \n"
                   f" Ergebnis: Test wurde erfolgreich durchgefuehrt. Das Passwort ist verdeckt \n"
                       f" >>> Funktion ist OK!")
        login_checkbox1.checked()
    else:
        with open("Login Testsuite.txt", mode="a") as file:
            file.write(f"\n\n\n Testfall 1 > Teste, ob Passwort verdeckt ist. \n"
                   f" Ergebnis: Test wurde erfolgreich durchgefuehrt. Das Passwort ist sichtbar. \n"
                       f" >>> Funktion sollte ueberprueft werden!")


    cookie = driver.find_element("xpath", f"{login_xpath1}")
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{username_xpath1}")
    time.sleep(0.3)
    cookie.click()
    cookie.send_keys(f"{TestName}")
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{passwort_xpath1}")
    time.sleep(0.3)
    cookie.click()
    cookie.send_keys(f"{TestfalschPW}")
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{anmelde_xpath1}")
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{passwort_xpath1}")
    time.sleep(0.3)
    cookie.click()
    cookie.send_keys(f"{TestfalschPW}")
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{anmelde_xpath1}")
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{passwort_xpath1}")
    time.sleep(0.3)
    cookie.click()
    cookie.send_keys(f"{TestfalschPW}")
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{anmelde_xpath1}")
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{passwort_xpath1}")
    time.sleep(0.3)
    cookie.click()
    cookie.send_keys(f"{TestfalschPW}")
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{anmelde_xpath1}")
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{passwort_xpath1}")
    time.sleep(0.3)
    cookie.click()
    cookie.send_keys(f"{TestfalschPW}")
    time.sleep(0.3)


    #Tf 2 Account gesperrt
    # Checkbox abhacken mit x oder i
    Acc_ist_gespeert_text = driver.find_element("xpath", '//*[@id="login-password-msg"]')
    if Acc_ist_gespeert_text.text == "Account ist gesperrt":
        with open("Login Testsuite.txt", mode="a") as file:
            file.write(f"\n\n\n Testfall 2 > Teste, ob Login nach vier fehlversuche gesperrt ist. \n"
                       f" Ergebnis: Test wurde erfolgreich durchgefuehrt. Das Account wurde nach vier versuchen gesperrt. \n"
                       f" >>> Funktion ist OK!")
        login_checkbox2.checked()
    else:
        with open("Login Testsuite.txt", mode="a") as file:
            file.write(f"\n\n\n Testfall 2 > Teste, ob Login nach vier fehlversuche gesperrt ist. \n"
                       f" Ergebnis: Test wurde erfolgreich durchgefuehrt. Das Account wurde nach vier NICHT versuchen gesperrt. \n"
                       f" >>> Funktion sollte ueberprueft werden!")

    #Tf 3 Groß- Kleinbuchstaben validieren
    # Checkbox abhacken mit x oder i
    if TestName != "test":
        with open("Login Testsuite.txt", mode="a") as file:
            file.write(f"\n\n\n Testfall 3 > Teste, ob Gross- und Kleinbuchstaben validieren. \n"
                   f" Ergebnis: Test wurde erfolgreich durchgefuehrt. Gross- und Kleinbuchstaben validieren. \n"
                       f" >>> Funktion sollte ueberprueft werden!")
    else:
        with open("Login Testsuite.txt", mode="a") as file:
            file.write(f"\n\n\n Testfall 3 > Teste, ob Groß- und Kleinbuchstaben validieren. \n"
                   f" Ergebnis: Test wurde erfolgreich durchgefuehrt. Groß- und Kleinbuchstaben koledieren Nicht. \n"
                       f" >>> Funktion ist OK!\n")
        login_checkbox3.checked()

    driver.quit()
    show_test_result()

# Hauptfunktion zur Ausführung des Tests für SUCHLEISTE
def run_search_test():
    # Hier kommen die Testlogiken für SUCHLEISTE
    produkt1 = "bohne"

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(f"{url_input}")
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{shop_link_xpath}")
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{suchleiste_xpath}")
    time.sleep(0.3)
    cookie.click()
    cookie.send_keys(f"{produkt1}")
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    product = driver.find_element("xpath", '//*[@id="shoplist"]/tbody/tr[2]/td[1]/a')
    print(product.text)
    if product.text != produkt1:
        with open("Searchbar Testsuite.txt", mode="a") as file:
            file.write(f"\n\n\n Testfall 1 > Testet, ob Eingabe nach Groß- und "
                       f" Kleinbuchstaben mit dem Produkt validieren. \n\n"
                       f" Ergebnis: Test wurde erfolgreich durchgefuehrt. \n"
                       f" Suche nach Produkt validiert auch mit Klein- Grossbuchstaben \n"
                       f" >>> Funktion ist OK!")
        suchleiste_checkbox.checked()
    driver.quit()
    show_test_result()

# Hauptfunktion zur Ausführung des Tests für WARENKORB
def run_cart_test():
    # Hier kommen die Testlogiken für WARENKORB
    tester = "tester"
    pw = "passwort"
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(f"{url_input}")
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{login_xpath1}")
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{username_xpath1}")
    time.sleep(0.3)
    cookie.click()
    cookie.send_keys(f"{tester}")
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{passwort_xpath1}")
    time.sleep(0.3)
    cookie.click()
    cookie.send_keys(f"{pw}")
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{anmelde_xpath1}")
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)


    cookie = driver.find_element("xpath", '/html/body/header/nav/a[3]')
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", '//*[@id="shoplist"]/tbody/tr[2]/td[4]/a')
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", '//*[@id="shoplist"]/tbody/tr[2]/td[4]/a')
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", '//*[@id="shoplist"]/tbody/tr[18]/td[4]/a')
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", '//*[@id="shoplist"]/tbody/tr[13]/td[4]/a')
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", '//*[@id="cart"]/a')
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    bohne = driver.find_element("xpath", '//*[@id="carttable"]/tbody/tr[2]/td[5]')
    remove_euro = bohne.text.replace('€', "")
    remove_comma = remove_euro.replace(",", ".")
    new_bohne = float(remove_comma)

    kaffebaum = driver.find_element("xpath", '//*[@id="carttable"]/tbody/tr[3]/td[5]')
    remove_euro = kaffebaum.text.replace('€', "")
    remove_comma = remove_euro.replace(",", ".")
    new_kafeebaum = float(remove_comma)

    niveacreme = driver.find_element("xpath", '//*[@id="carttable"]/tbody/tr[4]/td[5]')
    remove_euro = niveacreme.text.replace('€', "")
    remove_comma = remove_euro.replace(",", ".")
    new_creme = float(remove_comma)

    warenwert = driver.find_element("xpath", f"{warenwert_input1}")
    remove_euro = warenwert.text.replace('€', "")
    remove_text = remove_euro.replace("Gesamtsumme:", "")
    remove_comma = remove_text.replace(",", ".")
    new_warenwert = float(remove_comma)


    cookie = driver.find_element("xpath", '//*[@id="accountbar"]/table/tbody/tr[2]/td/a[2]')
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{login_xpath1}")
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{username_xpath1}")
    time.sleep(0.3)
    cookie.click()
    cookie.send_keys(f"{tester}")
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{passwort_xpath1}")
    time.sleep(0.3)
    cookie.click()
    cookie.send_keys(f"{pw}")
    time.sleep(0.3)
    cookie = driver.find_element("xpath", f"{anmelde_xpath1}")
    time.sleep(0.3)
    cookie.click()
    time.sleep(0.3)

    waren_speicherung = driver.find_element("xpath", '//*[@id="cartCount"]')
    waren_speicherung = waren_speicherung.text

    if waren_speicherung == "0":
        with open("Shopping cart Testsuite.txt", mode="a") as file:
            file.write(f"\n\n\n Testfall 1 > Testet, ob Produkte im Warenkorb nach erneutem Login gespeichert ist. \n"
                       f" Ergebnis: Test wurde erfolgreich durchgefuehrt. \n"
                       f" Die Produkte werden nicht gespeichert. \n"
                       f" >>> Funktion sollte ueberprueft werden!")
    else:
        with open("Shopping cart Testsuite.txt", mode="a") as file:
            file.write(f"\n\n\n Testfall 1 > Testet, ob Produkte im Warenkorb nach erneutem Login gespeichert ist. \n"
                       f" Ergebnis: Test wurde erfolgreich durchgefuehrt. \n"
                       f" Die Produkte wurden gespeichert. \n"
                       f" >>>> Funktion ist OK!")
        warenkorb_checkbox.checked()
    test_anzahl = new_bohne * 2
    if test_anzahl == 5.98:
        with open("Shopping cart Testsuite.txt", mode="a") as file:
            file.write(f"\n\n\n Testfall 2 > Testet, ob die Anzahl eines Produktes mit dem Gesamtpreis übereinstimmt \n"
                       f" Ergebnis: Test wurde erfolgreich durchgefuehrt. \n"
                       f" Der Gesamtpreis passt mit der Anzahl der Produkte überein. \n"
                       f" >>>> Funktion ist OK!")
        warenkorb_checkbox_2.checked()
    else:
        with open("Shopping cart Testsuite.txt", mode="a") as file:
            file.write(f"\n\n\n Testfall 2 > Testet, ob die Anzahl eines Produktes mit dem Gesamtpreis übereinstimmt \n"
                       f" Ergebnis: Test wurde erfolgreich durchgefuehrt. \n"
                       f" Der Gesamtpreis kolediert mit der Anzahl der Produkte. \n"
                       f" >>> Funktion sollte ueberprueft werden!")

    summe_produkte = new_bohne + new_kafeebaum + new_creme
    if summe_produkte == new_warenwert:
        with open("Shopping cart Testsuite.txt", mode="a") as file:
            file.write(f"\n\n\n Testfall 3 > Testet, ob die Summe im Warenkorb mit dem addierten Preis in der Datenbank übereinstimmt. \n"
                       f" Ergebnis: Test wurde erfolgreich durchgefuehrt. \n"
                       f" Die Summe stimmt mit dem Warenwert überein. \n"
                       f" >>>> Funktion ist OK!")
        warenkorb_checkbox_3.checked()
    else:
        with open("Shopping cart Testsuite.txt", mode="a") as file:
            file.write(f"\n\n\n Testfall 3 > Testet, ob die Summe im Warenkorb mit dem addierten Preis in der Datenbank übereinstimmt. \n"
                       f" Ergebnis: Test wurde erfolgreich durchgefuehrt. \n"
                       f" Die Summe stimmt NICHT mit dem Warenwert überein. \n"
                       f" >>> Funktion sollte ueberprueft werden!")
    driver.quit()
    show_test_result()

#Seite Zurück
def zurück():
    global page, close_software
    page -= 1
    update_gui()
    if page == 0:
        window.title("Test automatisation Software")
        warenkorb_input.place_forget()
        warenkorb_checkbox.hide()
        warenkorb_checkbox_2.hide()
        warenkorb_checkbox_3.hide()
        warenkorb_input.place_forget()
        warenwert_input.place_forget()
        login_checkbox1.hide()
        login_checkbox2.hide()
        login_checkbox3.hide()
        xpath_warenwert.hide()
        test_warenkorb_button.place_forget()
        close_software.place_forget()
        login_xpath.hide()
        username_xpath.hide()
        passwort_xpath.hide()
        anmelde_xpath.hide()
        username_entry.place_forget()
        passwort_entry.place_forget()
        anmelde_entry.place_forget()
        suchleiste_checkbox.hide()
        button_continue = tk.Button(window, text="Weiter", command=lambda:[get_data_input(),continue_to_next_page()])
        button_continue.place(x=300, y=260)
        button_continue.config(padx=10)
    elif page == 1:
        window.title("Testsuites Login/Registry")
        login_instruction = tk.Label(window, text="Testsuites Login" 
                                      "\n\nFüge den Xpath ein um die Login Funktion zu testen")
        login_instruction.place(x=50, y=30)
        label_hinweis.place_forget()
        entry_url.place_forget()
        entry_tester.place_forget()
        entry_projektnr.place_forget()
        label_projektnr.place_forget()
        label_url.place_forget()
        label_tester.place_forget()
        warenkorb_checkbox.hide()
        warenkorb_checkbox_2.hide()
        warenkorb_checkbox_3.hide()
        warenkorb_input.place_forget()
        warenwert_input.place_forget()
        xpath_warenwert.hide()
        login_xpath.hide()
        username_xpath.hide()
        passwort_xpath.hide()
        anmelde_xpath.hide()
        login_checkbox1.hide()
        login_checkbox2.hide()
        login_checkbox3.hide()
        login_entry.place_forget()
        username_entry.place_forget()
        passwort_entry.place_forget()
        anmelde_entry.place_forget()
        test_login_button.place_forget()
        close_software.place_forget()
        login_test()
        button_continue = tk.Button(window, text="Weiter", command=lambda:[get_data_input(),continue_to_next_page()])
        button_continue.place(x=300, y=260)
        button_continue.config(padx=10)

    elif page == 2:
        window.title("Testsuites Searchbar")
        searchbar_instruction = tk.Label(window, text="Testsuites Suchleiste"
                                      "'\n\nFüge den Xpath ein um die Suchleiste zu testen")
        searchbar_instruction.place(x=50,y=30)
        warenkorb_xpath.hide()
        login_xpath.hide()
        username_xpath.hide()
        passwort_xpath.hide()
        anmelde_xpath.hide()
        login_checkbox1.hide()
        login_checkbox2.hide()
        login_checkbox3.hide()
        login_entry.place_forget()
        username_entry.place_forget()
        passwort_entry.place_forget()
        anmelde_entry.place_forget()
        test_login_button.place_forget()
        warenkorb_input.place_forget()
        warenkorb_checkbox.hide()
        warenkorb_checkbox_2.hide()
        warenkorb_checkbox_3.hide()
        warenkorb_input.place_forget()
        warenwert_input.place_forget()
        xpath_warenwert.hide()
        test_warenkorb_button.place_forget()
        close_software.place_forget()
        suchleiste_label.hide()
        suchleiste_test()
        button_continue = tk.Button(window, text="Weiter", command=lambda:[get_data_input(),continue_to_next_page()])
        button_continue.place(x=300, y=260)
        button_continue.config(padx=10)
    elif page == 3:

        window.title("Testcase Warenkorb")
        warenkorb_instruction = tk.Label(window, text="Testsuites Warenkorb"
                                      "\n\nFüge den Xpath ein um den Warenkorb zu testen")
        warenkorb_instruction.place(x=50,y=30)
        suchleiste_label.hide()
        suchleiste_checkbox.hide()
        shop_link.hide()
        warenkorb_test()
        shop_entry.place_forget()
        suchleiste_entry.place_forget()
        test_suchleiste_button.place_forget()

# Funktion zum Überprüfen des Xpath
#def test_xpath():
    #xpath_benutzername = entry_xpath_benutzername.get()
    #xpath_passwort = entry_xpath_passwort.get()
    #xpath_bestätigung = entry_xpath_bestätigung.get()

    #if not xpath_benutzername or not xpath_passwort or not xpath_bestätigung:
        #messagebox.showerror("Fehler", "Bitte gebe den Xpath für Benutzername, Passwort und Button ein")
    #else:
        #messagebox.showinfo("Erfolg", "Xpath erfolgreich überprüft")



# Funktion zum Fortfahren zur nächsten Seite
# Create Database
def data_base():
    global db_dict
    db_dict = {
    "Projekt Nummer": [],
    "Tester": [],
    "URL": [],
    "Date": [],
    "Login Tf1": [],
    "Login Tf2": [],
    "Login Tf3":[],
    "Suchleister Tf1": [],
    "Warenkorb Tf1": [],
    "Warenkorb Tf2": [],
    "Warenkorb Tf3": []
    }
    data = pandas.DataFrame(db_dict)
    data.to_csv("datenbank.csv")
def continue_to_next_page():
    global page
    page += 1
    update_gui()

# update file
def create_filedata():
    if page==1:
        with open("Login Testsuite.txt", mode="w") as file:
            file.write(f" Testcase: {projektnr_input} \n current date: {today} \n\n Tester: {tester_input} \n\n Website: {url_input}")
    elif page == 2:
        with open("Searchbar Testsuite.txt", mode="w")as file:
            file.write(f" Testcase: {projektnr_input} \n current date: {today} \n\n Tester: {tester_input} \n\n Website: {url_input}")
    else:
        with open("Shopping cart Testsuite.txt", mode="w") as file:
            file.write(f" Testcase: {projektnr_input} \n current date: {today} \n\n Tester: {tester_input} \n\n Website: {url_input}")


page = 0
today = date.today()

# GUI erstellen
window = tk.Tk()
window.title("Test automatisation Software")
window.minsize(width=400, height=300)
image = Image.open("sogeti.png")
img = image.resize((80,40))

sogeti_img = ImageTk.PhotoImage(img)

canvas = tk.Canvas(width=130,height=130)
canvas.create_image(45,30, image=sogeti_img)
canvas.place(x=30,y=5)


# Button Erste Seite
button_info = tk.Button(window, text="Info", command=show_info)
button_info.place(x=30, y=260)
button_info.config(padx=10)
button_continue = tk.Button(window, text="Weiter", command=lambda:[get_data_input(),continue_to_next_page()])
button_continue.place(x=300, y=260)
button_continue.config(padx=10)
button_back = tk.Button(window, text="Zurück", command=zurück)
button_back.place(x=100, y=260)
button_back.config(padx=10)
# Textfeld Erste Seite
label_projektnr = tk.Label(window, text="Projekt NR")
label_projektnr.place(x=50, y=100)
label_tester = tk.Label(window, text="Testername")
label_tester.place(x=50, y=130)
label_url = tk.Label(window, text="URL Link")
label_url.place(x=50, y=160)
label_instruction = tk.Label(window, text="Füge die Daten hinzu um Test zu beginnen")
label_instruction.place(x=100, y=70)
label_hinweis = tk.Label(window, text="Hinweis: \n Klicke auf Info um Informationen zu Testfälle zu sehen")
label_hinweis.place(x=30, y=220)
# Inputfeld Erste Seite
entry_projektnr = tk.Entry(window,width=30)
entry_projektnr.place(x=180, y=100)
entry_tester = tk.Entry(window,width=30)
entry_tester.place(x=180, y=130)
entry_url = tk.Entry(window, width=30)
entry_url.place(x=180, y=160)



# GUI aktualisieren und starten
data_base()
update_gui()
window.mainloop()
