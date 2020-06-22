from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
        driver.get(self.url)

        total_height = driver.find_element("xpath", 'html').size["height"]
        driver.set_window_size(1920, total_height)

        driver.save_screenshot('screenshot.png')
        driver.close()


if __name__ == "__main__":
    url = 'https://dou.ua'
    ScreenShot(url).fullpage_screenshot()
