from selenium import webdriver
import time

# Inicjalizacje przeglądarki Chrome
driver = webdriver.Chrome()

# Otwarcie okna przeglądarki
driver.get('https://www.google.pl')

# Maksymalizacja okna
driver.maximize_window()

# Znajdowanie elementu by XPath - zaakceptuj zgody
accept = driver.find_element('xpath', '//*[@id="L2AGLb"]/div')
# Kliknięcie znalezionego elemntu
accept.click()

# Poczekaj 10 sekund, aby zobaczyć otwarte okno przeglądarki
# Sleep tylko do celów debugowych, testowych, nauczania
time.sleep(60)

# Zakończ działanie przeglądarki
driver.quit()  # zamknięcie wszystkich okien w przegladarce
# driver.close()  # zamknięcie danego okna przeglądarki


