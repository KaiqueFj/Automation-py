from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get( 'https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert('Selenium Easy Demo' in chrome_browser.title)

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')


assert('Show Message' in chrome_browser.page_source)

user_massage = chrome_browser.find_element_by_id('user-message')
user_massage.clear()
user_massage.send_keys('I am Python dev')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert('I am Python dev' in output_message.text)

print(user_button2)
print(show_message_button)
