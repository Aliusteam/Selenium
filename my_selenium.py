from selenium import webdriver
import time

# Переходим на сайт
browser = webdriver.Firefox()
#browser = webdriver.chrome()
browser.get('https://admin.evote75.dltc.spbu.ru/')
time.sleep(2)

# Выбраем наблюдателя
xpath = '/html/body/div/div[2]/div/div[6]/div/div[1]'
button = browser.find_element_by_xpath(xpath).click()
time.sleep(1)
xpath2 = '/html/body/div/div[2]/div/div[6]/div/div[2]/div[2]'
button = browser.find_element_by_xpath(xpath2).click()
#browser.save_screenshot('1.png')  # скриншот
time.sleep(1)

# Логин и пароль
xpath = '/html/body/div/div[2]/div/div[6]/form/div[1]/div[2]/input'
button = browser.find_element_by_xpath(xpath).send_keys('cisan80356@onzmail.com')
time.sleep(1)
xpath = '/html/body/div/div[2]/div/div[6]/form/div[2]/div[2]/input'
button = browser.find_element_by_xpath(xpath).send_keys('Qq123456')
time.sleep(1)

# жмем на вход
xpath = '/html/body/div/div[2]/div/div[6]/form/div[8]/div/div'
button = browser.find_element_by_xpath(xpath).click()
time.sleep(3)

# Переходим в личный кабинет
browser.get('https://admin.evote75.dltc.spbu.ru/users/cisan80356@onzmail.com')
time.sleep(2)

# Смена пароля в личном кабинете
xpath = '/html/body/div[2]/div[3]/div[2]/div/div[4]/div/div[2]/div/div[3]/div[2]/div[1]/div/input'
button = browser.find_element_by_xpath(xpath).send_keys('Qq123456')
time.sleep(1)

xpath = '/html/body/div[2]/div[3]/div[2]/div/div[4]/div/div[2]/div/div[3]/div[2]/div[3]/div/input'
button = browser.find_element_by_xpath(xpath).send_keys('Qq123456')
time.sleep(1)

# Нажимаем сохранить
xpath = '/html/body/div[2]/div[3]/div[2]/div/div[5]/div/div'
button = browser.find_element_by_xpath(xpath).click()
#browser.refresh()
time.sleep(3)

browser.quit()