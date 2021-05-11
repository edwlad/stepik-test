from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')

    el = browser.find_element_by_id('treasure')
    temp = str(math.log(abs(12*math.sin(int(el.get_attribute('valuex'))))))
    browser.find_element_by_id('answer').send_keys(temp)

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button.btn').click()

    time.sleep(30)

except Exception as e:
    print(f'Error: {type(e).__name__}\n{e}')

finally:
    browser.quit()
