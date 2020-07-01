import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidArgumentException


class ScreenShot:
    """Class for a screenshot`s management."""
    def __init__(self, url):
        self.url = url

    def fullpage_screenshot(self):
        """Take a screenshot."""
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--test-type')
        options.add_argument('--headless')
        options.add_argument('--start-maximized')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')
        driver = webdriver.Chrome(chrome_options=options)

        def _scroll_size(size):
            """Get window`s size after scrolling"""
            return driver.execute_script('return document.body.parentNode.scroll' + size)

        try:
            driver.get(self.url)
        except InvalidArgumentException:
            driver.get(f'https://{self.url}')

        driver.set_window_size(_scroll_size('Width'), _scroll_size('Height'))
        driver.find_element_by_tag_name('body')
        driver.save_screenshot(f'{self.get_photo_name()}.png')
        driver.close()

    def get_photo_name(self):
        """Create a name for photo file."""
        return abs(hash(self.url))

    def delete_photo(self):
        """Delete photo file after sending"""
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            f'{self.get_photo_name()}.png')
        os.remove(path)
