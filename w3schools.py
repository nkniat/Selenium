from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# Inicjalizacje przeglądarki Chrome
driver = webdriver.Chrome()

# Implicity wait (lepszy niż sleep)
# Jeśli nie znajdziesz danego elemtnu, to poczekaj na niego 10 sekund.
# Jeśli znajdziesz element, to leć dalej
# definiujemy raz na cały projekt
# driver.implicitly_wait(10)

# Explicity wait (lepszy niż implicity, dynamiczny)
# pamiętaj o imporcie biblioteki WebDriverWait
wait = WebDriverWait(driver, 10, 0.5, NoSuchElementException)

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
# uzycie waita dla danego elementu
wait.until(expected_conditions.visibility_of_element_located(('xpath', '//*[@id="leftmenuinnerinner"]/a[39]')))
# wait z własnym zdefiniowanym warunkiem (wykorzystujemy lambde i niezerowa dlugosc listy)
# wait.until(lambda x: len(x.find_elements('xpath', '//*[@id="leftmenuinnerinner"]/a[39]')))
forms = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[39]')
forms.click()

# Poczekaj 10 sekund, aby zobaczyć otwarte okno przeglądarki
# Sleep tylko do celów debugowych, testowych, nauczania
time.sleep(600)

# Zakończ działanie przeglądarki
driver.quit()  # zamknięcie wszystkich okien w przegladarce

