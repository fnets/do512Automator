from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://do512.com/events/2016/8/19/i-m-not-mad-sketch-comedy-feat-the-conspirators")
try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.ds-btn.stretch.ds-btn-large.ds-btn-ical.ds-follow"))
    )
finally:
    browser.quit()
elem = browser.find_element_by_class_name("ds-btn.stretch.ds-btn-large.ds-btn-ical.ds-follow" ).click() #connection is rejected after this call, not sure why
browser.close()