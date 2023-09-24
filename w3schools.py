from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Inicjalizacje przeglądarki Chrome
driver = webdriver.Chrome()

# Otwarcie okna przeglądarki
driver.get('https://www.w3schools.com/')
print("Tytuł bieżącego okna przeglądarki to: ", driver.title)

driver.maximize_window()

# Akceptacje warunkow
accept = driver.find_element('id', 'accept-choices')
accept.click()

# Menu HTML (lewy gorny rog)
menu = driver.find_element('xpath', '//*[@id="subtopnav"]/a[1]')
menu.click()

# HTML Forms
forms = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[39]')
forms.click()

# Poczekaj 10 sekund, aby zobaczyć otwarte okno przeglądarki
# Sleep tylko do celów debugowych, testowych, nauczania
time.sleep(600)

# Zakończ działanie przeglądarki
driver.quit()  # zamknięcie wszystkich okien w przegladarce

