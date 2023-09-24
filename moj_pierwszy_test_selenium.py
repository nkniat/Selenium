from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Inicjalizacje przeglądarki Chrome
driver = webdriver.Chrome()

# Otwarcie okna przeglądarki
driver.get('https://www.google.pl')

# Maksymalizacja okna
driver.maximize_window()
driver.set_window_size(1600, 800)

# Znajdowanie elementu by XPath - zaakceptuj zgody
accept = driver.find_element('xpath', '//*[@id="L2AGLb"]/div')
# Kliknięcie znalezionego elemntu
accept.click()

# Znajdź pole wyszukiwania
search_box = driver.find_element('name', 'q')

# Wprowadzanie hasła do wyszukiwarki
search_box.send_keys('Pogoda Kraków')

# Naciśnij Enter
search_box.send_keys(Keys.ENTER)

# Poczekaj 10 sekund, aby zobaczyć otwarte okno przeglądarki
# Sleep tylko do celów debugowych, testowych, nauczania
time.sleep(600)

# Zakończ działanie przeglądarki
driver.quit()  # zamknięcie wszystkich okien w przegladarce
# driver.close()  # zamknięcie danego okna przeglądarki


