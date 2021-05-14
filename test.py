from selenium import webdriver
from selenium.webdriver.common.keys import Keys

capabilities = {
    "browserName": "chrome",
    "version": "78.0",
    "platform": "LINUX"
}

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=capabilities
)

try:
    print 'Session ID is: %s' % driver.session_id
    print 'Opening the page...'
    driver.get('https://duckduckgo.com/')

    print 'Taking screenshot...'
    driver.get_screenshot_as_file(driver.session_id + '.png')
finally:
    driver.quit()