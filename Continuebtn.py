from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implisitly_wait(20)


driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")
driver.maximize_window()
new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")
new_registrant_btn.click()
 #wait for Continue button to click
wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Continue')]")))
    #title register account to be visible
logo=driver.find_element_by_xpath("//*[@id='content']/h1")
wd_wait=WebDriverWait(driver,20)
element=WebDriverWait(driver,20).until(EC.title_is(("Register Account")))





