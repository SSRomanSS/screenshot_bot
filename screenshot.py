import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidArgumentException


class ScreenShot:
    def __init__(self, url):
        self.url = url

    def fullpage_screenshot(self):
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--test-type')
        options.add_argument('--headless')
        options.add_argument('--start-maximized')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')
        driver = webdriver.Chrome(chrome_options=options)
        try:
            driver.get(self.url)
        except InvalidArgumentException:
            driver.get(f'https://{self.url}')

        total_height = driver.find_element("xpath", 'html').size["height"]
        driver.set_window_size(1920, total_height)
        driver.save_screenshot(f'{self.get_photo_name()}.png')
        driver.close()

    def get_photo_name(self):
        return abs(hash(self.url))

    def delete_photo(self):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{self.get_photo_name()}.png')
        os.remove(path)



