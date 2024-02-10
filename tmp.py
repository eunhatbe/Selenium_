import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver_path = ""

# 브라우저 자동 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)
driver.get("https://store.steampowered.com/login/?redir=&redir_ssl=1&snr=1_4_4__global-header")

driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div[3]/div[2]/div[1]/a/span').click()
driver.implicitly_wait(1)

driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("")
driver.find_element(By.XPATH, '//*[@id="reenter_email"]').send_keys("")

driver.find_element(By.XPATH, '//*[@id="i_agree_check"]').click()
time.sleep(2)

iframe = driver.find_element(By.TAG_NAME, "iframe")

driver.switch_to.frame(iframe)
time.sleep(2)
print("switch")
driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]').click()

# //*[@id="recaptcha-anchor"]/div[1]
