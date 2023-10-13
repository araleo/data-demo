import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


cursor_script = '''
var cursor = document.createElement('div');
cursor.style.position = 'absolute';
cursor.style.zIndex = '9999';
cursor.style.width = '50px';
cursor.style.height = '50px';
cursor.style.borderRadius = '50%';
cursor.style.backgroundColor = 'transparent';
cursor.style.pointerEvents = 'none';
document.body.appendChild(cursor);

document.addEventListener('mousedown', (e) => {
  cursor.style.left = e.pageX - 25 + 'px';
  cursor.style.top = e.pageY - 25 + 'px';
  cursor.style.border = '1px solid steelblue';

  setTimeout(() => {
    cursor.style.border = '0';
  }, 750)
});
'''

APP_URL = "http://host.docker.internal:5173/editor"

WAIT_DELAY = 2


def main():
    options = FirefoxOptions()
    browser = webdriver.Remote("http://localhost:4444/wd/hub", options=options)
    browser.get(APP_URL)
    action = ActionChains(browser)
    browser.execute_script(cursor_script)
    elements = browser.find_elements(By.CSS_SELECTOR, "[data-demo]")

    for element in elements:
        action.move_to_element(element).click().perform()
        time.sleep(WAIT_DELAY)
        action.move_to_element(element).click().perform()

    browser.close()


if __name__ == "__main__":
    main()
